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
