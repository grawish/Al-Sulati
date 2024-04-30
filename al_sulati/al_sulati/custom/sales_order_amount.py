import frappe

@frappe.whitelist()
def fetch_custom_rate(doctype, fieldname, prevdoc_docname,item_code):
    rate = frappe.db.get_value(doctype, {'parent': prevdoc_docname, 'item_code': item_code}, fieldname)
    return rate
