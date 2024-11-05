from frappe.model.document import Document
import frappe
import json

@frappe.whitelist()
def fetch_serial_no(doc):
    doc_obj = json.loads(doc)

    serial_no_doc = frappe.get_doc("Serial and Batch Bundle", doc_obj['custom_serial_no'])
    serial_no_details = serial_no_doc.get("entries")
    project=frappe.get_doc("Project", doc_obj["parent_project"])
    custom_rate=project.custom_rate
    serial_no_data = []
    data={}
    for  item in  serial_no_details:
        data = {
            "serial_no": item.serial_no,   
            "custom_rate":custom_rate
        }
        serial_no_data.append(data)

    return serial_no_data


@frappe.whitelist()
def fetch_project_details(project):
    project_doc = frappe.get_doc("Project", project)
    if project_doc:
        return {
            
            "customer": project_doc.customer,
            "company": project_doc.company,
            
        }
    else:
        return None
        





