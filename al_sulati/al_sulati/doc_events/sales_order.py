import frappe


def before_save(doc, method):
    exists = []
    for mach in doc.custom_machine_allocation:
        machine = frappe.get_doc('Machine', mach.machine)
        if machine.status != 'Available':
            frappe.throw('Machine Not Available')
        if mach.machine in exists:
            frappe.throw('Duplicate Machine Not Allowed')
        else:
            exists.append(mach.machine)


def on_submit(doc, method):
    for mach in doc.custom_machine_allocation:
        machine = frappe.get_doc('Machine', mach.machine)
        machine.status = 'Engaged'
        machine.save(ignore_permissions=True)
    #For Employee Doc.
    for emp in doc.custom_employee:
        employee = frappe.get_doc('Employee', emp.employee_name)
        employee.custom_sales_order_id = doc.name  # Accessing the Sales Order ID
        employee.custom_employee_availabilty = "Engaged"
        employee.date = doc.transaction_date 
        employee.custom_customer_name = doc.customer
        employee.save(ignore_permissions=True)

