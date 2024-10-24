// Copyright (c) 2024, Hybrowlabs Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Supplier Contract', {
    from_date: function(frm) {
        calculate_valid_till(frm);
    },
    to_date: function(frm) {
        calculate_valid_till(frm);
    }
});

function calculate_valid_till(frm) {
    const fromDate = frm.doc.from_date;
    const toDate = frm.doc.to_date;

    if (fromDate && toDate) {
        const startDate = new Date(fromDate);
        const endDate = new Date(toDate);
        const differenceInTime = endDate.getTime() - startDate.getTime();
        const differenceInDays = differenceInTime / (1000 * 3600 * 24);

        frm.set_value('valid_till', differenceInDays);
    } else {
        frm.set_value('valid_till', 0);
    }
}
