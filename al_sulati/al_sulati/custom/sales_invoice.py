import frappe

@frappe.whitelist()
def fetch_timesheet_details(timesheet):
    timesheet_doc = frappe.get_doc('Timesheet', timesheet)
    project = timesheet_doc.project
    customer = timesheet_doc.customer
    registration_no = timesheet_doc.registration_no
    total_billing_hours = timesheet_doc.total_billing_hours

    # Fetch item code based on registration number
    item_code = frappe.db.get_value('Item', {'registration_no': registration_no}, 'item_code')

    # Fetch item details
    items = []
    for detail in timesheet_doc.time_logs:
        item = {
            "item_code": item_code,  # Use fetched item code
            "qty": detail.qty,
            "rate": detail.billing_rate,
            "registration_no": registration_no
            # Add other fields if necessary
        }
        items.append(item)

    return {
        'project': project,
        'customer': customer,
        'items': items,
        'registration_no': registration_no,
        'total_billing_hours': total_billing_hours
    }


