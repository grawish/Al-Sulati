frappe.ui.form.on('Purchase Order', {
    onload(frm) {
        if (frm.doc.custom_no_active_contract) {
            frm.dashboard.set_headline_alert(
                __('No active supplier contract for this supplier.'),
                'orange'
            );
        }
    }
});
