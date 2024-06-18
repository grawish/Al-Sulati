frappe.ui.form.on("Timesheet", {
    onload: function(frm) {

        // if (frm.doc.parent_project) {
        //     populate_project_details(frm, frm.doc.parent_project);
        // }

        
        frm.set_query("custom_serial_no", function() {
            return {
                filters: {
                    custom_project: frm.doc.parent_project,
                }
            };
        });
    },

    // parent_project: function(frm) {
    //     if (frm.doc.parent_project) {
    //         populate_project_details(frm, frm.doc.parent_project);
    //     }
    // },
 

    custom_serial_no: function(frm) {
        if (frm.doc.custom_serial_no) {
            frappe.call({
                method: 'al_sulati.al_sulati.custom.timesheet.fetch_serial_no',
                args: {
                    doc: frm.doc
                },
                callback: function(response) {
                    console.log(response);
                    if (response.message) {
                        // Populate the reg_no field as a dropdown with the fetched registration numbers
                        let options = response.message.map(item => item.serial_no);
                        frm.set_df_property('reg_no', 'options', options.join('\n'));
                        frm.set_value('reg_no', options[0]); // Set the first option as the default value
                        
                        // Populate the time_logs table based on the default reg_no
                        update_time_logs(frm, response.message, options[0]);
                    } else {
                        frm.set_df_property('reg_no', 'options', '');
                        frm.set_value('reg_no', ''); // Clear the reg_no field if no options are available
                    }
                }
            });
        } else {
            frm.set_df_property('reg_no', 'options', '');
            frm.set_value('reg_no', ''); // Clear the reg_no field if custom_serial_no is not selected
        }
    },

    reg_no: function(frm) {
        if (frm.doc.reg_no) {
            frappe.call({
                method: 'al_sulati.al_sulati.custom.timesheet.fetch_serial_no',
                args: {
                    doc: frm.doc
                },
                callback: function(response) {
                    console.log(response);
                    if (response.message) {
                        // Populate the time_logs table based on the selected reg_no
                        update_time_logs(frm, response.message, frm.doc.reg_no);
                    }
                }
            });
        }
    }
});


// function populate_project_details(frm, project) {
//     frappe.call({
//         method: 'al_sulati.al_sulati.custom.timesheet.fetch_project_details',
//         args: {
//             project: project
//         },
//         callback: function(response) {
//             if (response.message) {
//                 frm.set_value('project_name', response.message.project_name);
//                 frm.set_value('customer', response.message.customer);
//                 frm.set_value('company', response.message.company);
//                 frm.set_value('currency', response.message.currency);
//                 frm.set_value('serial_no', response.message.serial_no);
//             }
//         }
//     });
//  }
 

function update_time_logs(frm, serial_no_data, selected_reg_no) {
    frm.clear_table("time_logs");
    serial_no_data.forEach(item => {
        if (item.serial_no === selected_reg_no) {
            const newRow = frappe.model.add_child(frm.doc, "time_logs");
            newRow.custom_registration_no = item.serial_no;
            newRow.project = frm.doc.parent_project;
            newRow.billing_rate = item.custom_rate;
        }
    });
    frm.refresh_field('time_logs');
}
