import frappe

@frappe.whitelist()
def fetch_active_employee_signature():
    # Fetch the active Employee's signature
    employee = frappe.get_all('Employee',
                              filters={'status': 'Active'},
                              fields=['name', 'custom_signature'],
                              order_by='creation desc',
                              limit=1)

    if employee:
        return employee[0].custom_signature

    return None