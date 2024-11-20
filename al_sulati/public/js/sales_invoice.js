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




frappe.ui.form.on('Sales Invoice', {
    onload: function(frm) {
        let displayed_po = [];  

        frm.doc.items.forEach(item => {
            if (item.sales_order && !displayed_po.includes(item.sales_order)) {
                frappe.db.get_value('Purchase Order', {'custom_sales_order_id': item.sales_order}, 'name')
                    .then(r => {
                        if (r && r.message && r.message.name) {
                            const po_name = r.message.name;
                            frappe.db.count('Purchase Invoice Item', {
                                filters: {
                                    'purchase_order': po_name,
                                    'docstatus': 1 
                                }
                            }).then(count => {
                                if (count === 0 && !displayed_po.includes(po_name)) {
                                    displayed_po.push(po_name);

                                    frm.dashboard.set_headline_alert(
                                        __('Please create a Purchase Invoice against this Purchase Order: <a href="/app/purchase-order/{0}" ">{0}</a>', [po_name]),
                                        'orange'
                                    );
                                }
                            });
                        }
                    });
            }
        });
    }
});
