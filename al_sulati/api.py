import frappe

@frappe.whitelist()
def delete_invoice(invoice):
  frappe.db.delete("Sales Invoice", invoice)
  frappe.db.commit()
