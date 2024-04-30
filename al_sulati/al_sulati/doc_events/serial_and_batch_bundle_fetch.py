import frappe

def before_save(doc,method):
    
    if len(doc.project):
        if doc.items:
            for i in doc.items:
                serial_batch = i.serial_and_batch_bundle
                frappe.db.set_value("Serial and Batch Bundle", serial_batch, {
                    "custom_project" : doc.project
                })