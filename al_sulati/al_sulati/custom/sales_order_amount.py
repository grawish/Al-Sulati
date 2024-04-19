import frappe

@frappe.whitelist()
def fetch_custom_rate(doctype, fieldname, prevdoc_docname):
    rate = frappe.db.get_value(doctype, {'parent': prevdoc_docname}, fieldname)
    return rate
