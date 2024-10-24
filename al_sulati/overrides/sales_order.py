import frappe
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder
from erpnext.controllers.accounts_controller import AccountsController

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
                }, fields=['name'])
                
                if supplier_contract:
                    contract_doc = frappe.get_doc("Supplier Contract", supplier_contract[0].name)
                    for rate_row in contract_doc.table_rypr:
                        if rate_row.rate_type == item.custom_rate_selection:
                            create_purchase_order(doc, item.custom_custom_supplier, rate_row.rate)
                            break  

def create_purchase_order(sales_order, supplier_name, rate):
    po_doc = frappe.new_doc("Purchase Order")
    po_doc.supplier = supplier_name
    po_doc.schedule_date = sales_order.delivery_date or frappe.utils.nowdate()
    
    for item in sales_order.items:
        if item.custom_custom_supplier == supplier_name:
            po_item = po_doc.append("items", {})
            po_item.item_code = item.item_code
            po_item.qty = item.qty
            po_item.rate = rate  
            po_item.schedule_date = item.delivery_date or frappe.utils.nowdate()

    po_doc.save()
    po_doc.submit()
    frappe.msgprint(f"Purchase Order {po_doc.name} created for Supplier: {supplier_name}")

# Override the validate_payment_schedule_dates method for Sales Orders only
def override_validate_payment_schedule_dates(self, *args, **kwargs):
    if self.doctype == "Sales Order":
        pass
    else:
        original_validate_payment_schedule_dates(self, *args, **kwargs)

original_validate_payment_schedule_dates = AccountsController.validate_payment_schedule_dates
AccountsController.validate_payment_schedule_dates = override_validate_payment_schedule_dates
