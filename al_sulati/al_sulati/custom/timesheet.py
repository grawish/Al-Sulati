from frappe.model.document import Document
import frappe
import json



@frappe.whitelist()
def fetch_serial_no(doc):
    doc_obj = json.loads(doc)
    serial_no_doc = frappe.get_doc("Serial and Batch Bundle", doc_obj['custom_serial_no'])
    serial_no_details = serial_no_doc.get("entries")
    serial_no_data = []
    data={}
    for  item in  serial_no_details:
        data = {
            "serial_no": item.serial_no,   
        }

        serial_no_data.append(data)

    return serial_no_data