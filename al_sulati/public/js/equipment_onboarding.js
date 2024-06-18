frappe.ui.form.on('Purchase Receipt', {
    refresh(frm) {
        
        setTimeout(() => {

        frm.remove_custom_button('Purchase Return', 'Create');
        frm.remove_custom_button('Purchase Invoice', 'Create');
        frm.remove_custom_button('Make Stock Entry', 'Create');
        frm.remove_custom_button('Retention Stock Entry', 'Create');
        
        

    }, 1000);
        // Add only the "Sales Order" option to the "Create" button
        frm.page.add_inner_button(__('Sales Order'), function() {
            frappe.new_doc('Sales Order');
        }, 'Create');
    }
});

