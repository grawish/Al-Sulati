# your_app/your_module.py
import frappe

@frappe.whitelist()
def get_sales_order_items(project):
    sales_order_items = []
    # Fetch Sales Orders linked to the project
    sales_orders = frappe.get_all('Sales Order', filters={'project': project}, fields=['name'])
    for so in sales_orders:
        # Fetch Sales Order items
        items = frappe.get_all('Sales Order Item', filters={'parent': so.name}, fields=['item_code', 'item_name', 'custom_rate_selection', 'rate'])
        sales_order_items.extend(items)
    return sales_order_items
