import frappe
import json

@frappe.whitelist()
def updateEmpStatus(doc):
    doc_obj=json.loads(doc)
    for emp in doc_obj['custom_employee']:
        emp_doc=frappe.get_doc("Employee",emp['employee_name'])
        if emp_doc:
            emp_doc.custom_employee_availabilty = "Engaged"
            emp_doc.save()


   
