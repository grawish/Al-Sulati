frappe.ui.form.on('Timesheet', {
    create_sales_invoice: function(frm) {
        // Fetch timesheet details and create Sales Invoice
        frappe.call({
            method: "al_sulati.al_sulati.custom.sales_invoice.fetch_timesheet_details",
            args: {
                timesheet: frm.doc.name
            },
            callback: function(r) {
                if (r.message) {
                    // Create new Sales Invoice with fetched data
                    frappe.model.with_doctype('Sales Invoice', function() {
                        var si = frappe.model.get_new_doc('Sales Invoice');
                        si.customer = r.message.customer;
                        si.project = r.message.project;
                        si.registration_no = r.message.registration_no;
                        si.total_billing_hours = r.message.total_billing_hours;

                        // Populate items
                        if (r.message.items && r.message.items.length > 0) {
                            r.message.items.forEach(function(item) {
                                var item_row = frappe.model.add_child(si, 'items');
                                item_row.item_code = item.item_code;
                                item_row.qty = item.qty;
                                item_row.rate = item.rate;
                                item_row.registration_no = item.registration_no;
                            });
                        }

                        // Redirect to new Sales Invoice
                        frappe.set_route('Form', 'Sales Invoice', si.name);
                    });
                }
            }
        });
    }
});
