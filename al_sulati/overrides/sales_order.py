import frappe
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder
from erpnext.controllers.accounts_controller import AccountsController
from frappe.utils import nowdate, getdate
from datetime import datetime
from frappe.utils import flt,money_in_words

def on_submit_sales_order_wrapper(doc, method):
    create_po_on_submit(doc)

def create_po_on_submit(doc):
    for item in doc.items:
        if item.custom_custom_supplier:
            supplier = frappe.get_doc("Supplier", item.custom_custom_supplier)
            if supplier.supplier_type != "Individual":
                supplier_contract = frappe.get_all('Supplier Contract', filters={
                    'supplier': item.custom_custom_supplier,
                    'item': item.item_code
                }, fields=['name', 'to_date'])

                if supplier_contract:
                    contract_doc = frappe.get_doc("Supplier Contract", supplier_contract[0].name)
                    for rate_row in contract_doc.table_rypr:
                        if rate_row.rate_type == item.custom_rate_selection:
                            # Convert delivery_date to datetime for comparison
                            delivery_date = datetime.strptime(doc.delivery_date, '%Y-%m-%d').date()

                            # Check delivery date against contract's to_date
                            if delivery_date > contract_doc.to_date:
                                rate = 0  # Set rate to 0 if delivery date exceeds contract's to_date
                                custom_no_active_contract = 1
                            else:
                                rate = rate_row.rate
                                custom_no_active_contract = 0
                            
                            # Create Purchase Order with appropriate rate and contract status
                            create_purchase_order(doc, item.custom_custom_supplier, rate, custom_no_active_contract)
                            break  

def create_purchase_order(sales_order, supplier_name, rate, custom_no_active_contract):
    po_doc = frappe.new_doc("Purchase Order")
    po_doc.supplier = supplier_name
    po_doc.custom_sales_order_id = sales_order.name  # Set custom_sales_order_id with Sales Order name
    po_doc.schedule_date = sales_order.delivery_date or frappe.utils.nowdate()
    po_doc.custom_no_active_contract = custom_no_active_contract  # Set contract status based on date check

    for item in sales_order.items:
        if item.custom_custom_supplier == supplier_name:
            po_item = po_doc.append("items", {})
            po_item.item_code = item.item_code
            po_item.qty = item.qty
            po_item.rate = rate  # Set the initial rate
            po_item.amount = rate * item.qty  # Calculate amount based on rate
            po_item.schedule_date = item.delivery_date or frappe.utils.nowdate()

    po_doc.save()
    po_doc.submit()
    frappe.msgprint(f"Purchase Order {po_doc.name} created for Supplier: {supplier_name}")

     # Directly set rate to 0 in the database after submission if no active contract
    if custom_no_active_contract:
        for po_item in po_doc.items:
            frappe.db.set_value("Purchase Order Item", po_item.name, "qty", 0)
            frappe.db.set_value("Purchase Order Item", po_item.name, "rate", 0)
            frappe.db.set_value("Purchase Order Item", po_item.name, "amount", 0)
        # frappe.msgprint("Rates set to 0 due to inactive supplier contract.")

        po_doc.total = 0
        po_doc.grand_total= 0
        po_doc.rounded_total = round(po_doc.grand_total)
        po_doc.in_words = frappe.utils.money_in_words(po_doc.grand_total)
        po_doc.db_update()


   


        
# Override the validate_payment_schedule_dates method for Sales Orders only
def override_validate_payment_schedule_dates(self, *args, **kwargs):
    if self.doctype == "Sales Order":
        pass
    else:
        original_validate_payment_schedule_dates(self, *args, **kwargs)

original_validate_payment_schedule_dates = AccountsController.validate_payment_schedule_dates
AccountsController.validate_payment_schedule_dates = override_validate_payment_schedule_dates
