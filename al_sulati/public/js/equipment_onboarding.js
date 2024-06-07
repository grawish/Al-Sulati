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

// frappe.ui.form.on('Equipment Onboarding', {
//     refresh: function(frm) {
//         // Remove existing create options
//         frm.page.clear_primary_action();

//         // Add custom button for creating Sales Order
//         frm.page.add_custom_button(__('Create Sales Order'), function() {
//             frappe.call({
//                 method: "al_sulati.al_sulati.custom.sales_order.fetch_equipment_details",
//                 args: {
//                     onboarding: frm.doc.name
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         // Create new Sales Order with fetched data
//                         frappe.model.with_doctype('Sales Order', function() {
//                             var so = frappe.model.get_new_doc('Sales Order');
//                             so.customer = r.message.customer;
//                             so.project = r.message.project;
                            
//                             // Populate items
//                             if (r.message.items && r.message.items.length > 0) {
//                                 r.message.items.forEach(function(item) {
//                                     var item_row = frappe.model.add_child(so, 'items');
//                                     item_row.item_code = item.item_code;
//                                     item_row.qty = item.qty;
//                                     item_row.rate = item.rate;
//                                 });
//                             }

//                             // Redirect to new Sales Order
//                             frappe.set_route('Form', 'Sales Order', so.name);
//                         });
//                     }
//                 }
//             });
//         });
//     }
// });
