import frappe

@frappe.whitelist()
def fetch_equipment_details(onboarding):
    onboarding_doc = frappe.get_doc('Equipment Onboarding', onboarding)
    project = onboarding_doc.project
    customer = onboarding_doc.supplier

    # Fetch item details
    items = []
    for equipment in onboarding_doc.equipment_details:
        item = {
            "item_code": equipment.item_code,
            "qty": equipment.qty,  # Adjust based on your document's field names
            "rate": equipment.rate  # Adjust based on your document's field names
        }
        items.append(item)

    return {
        'project': project,
        'customer': customer,
        'items': items
    }

