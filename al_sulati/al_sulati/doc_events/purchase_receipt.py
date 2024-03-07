import frappe

@frappe.whitelist()
def get_all_serials(**kwargs):
    name = kwargs.get("name")
    doc = frappe.get_doc("Purchase Receipt", name)
    all_serials = []
    for item in doc.items:
        serials = []
        bundle = item.serial_and_batch_bundle
        if bundle is not None:
            bundle_doc = frappe.get_doc("Serial and Batch Bundle", bundle)
            for entry in bundle_doc.entries:
                serials.append(entry.serial_no)
        else:
            serials = item.serial_no.split('\n')
        all_serials.extend(serials)
    return all_serials