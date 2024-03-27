frappe.ui.form.on("Purchase Receipt", {
    onload: (frm) => {
        console.log('load');
    },
    refresh: (frm) => {
        console.log('refresh');
    },
    on_submit: (frm) => {
        frappe.call({
            method: "al_sulati.al_sulati.doc_events.purchase_receipt.get_all_serials",
            args: {
                name: frm.doc.name
            },
            callback: (data) => {
                const serials = data.message;
                const fields = [];

                serials.forEach((serial) => {
                    fields.push({
                        label: "Serial No",
                        fieldtype: "Read Only",
                        fieldname: "serial_no_" + serial,
                        default: serial
                    });

                    fields.push({
                        label: "Attachment",
                        fieldtype: "Attach",
                        fieldname: "attach_" + serial
                    });

                    fields.push({
                        label: "Brand Name",
                        fieldtype: "Link",
                        options: "Brand",
                        fieldname: "brand_name_" + serial
                    });

                    fields.push({
                        label: "Model Name",
                        fieldtype: "Data",
                        fieldname: "model_name_" + serial
                    });

                    fields.push({
                        label: "Registration Expiry Date",
                        fieldtype: "Date",
                        fieldname: "registration_expiry_date_" + serial
                    });

                    fields.push({
                        label: "Attachments",
                        fieldtype: "Attach",
                        fieldname: "attachments_" + serial
                    });

                    fields.push({
                        label: "Insurance Expiry Date",
                        fieldtype: "Date",
                        fieldname: "insurance_expiry_date_" + serial
                    });

                    fields.push({
                        label: "Attachments(Insurance)",
                        fieldtype: "Attach",
                        fieldname: "attachmentinsurance_" + serial
                    });

                    fields.push({
                        label: "PPC Expiry Date",
                        fieldtype: "Date",
                        fieldname: "ppc_expiry_date_" + serial
                    });

                    fields.push({
                        label: "Attachments(PPC)",
                        fieldtype: "Attach",
                        fieldname: "aattachmentppc_" + serial
                    });

                    fields.push({
                        label: "Warranty Expiry Date",
                        fieldtype: "Date",
                        fieldname: "warranty_expiry_date_" + serial
                    });

                    fields.push({
                        label: "AMC Expiry Date",
                        fieldtype: "Date",
                        fieldname: "amc_expiry_date_" + serial
                    });
                });

                const dialog = new frappe.ui.Dialog({
                    title: __("Serials Attachment"),
                    fields: fields,
                    primary_action_label: "Save",
                    primary_action: async (values) => {
                        serials.forEach((serial) => {
                            frappe.db.set_value(
                                "Serial No", // DocType
                                serial, // Document name
                                { // Field-value dictionary
                                    "custom_attachments": values['attach_' + serial],
                                    "custom_brand_name": values['brand_name_' + serial],
                                    "custom_model_name": values['model_name_' + serial],
                                    "custom_registration_expiry_date": values['registration_expiry_date_' + serial],
                                    "custom_attachments": values['attachments_' + serial],
                                    "custom_insurance_expiry_date_": values['insurance_expiry_date_' + serial],
                                    "custom_attachmentsinsurance": values['attachmentinsurance_' + serial],
                                    "custom_ppc_expiry_date_": values['ppc_expiry_date_' + serial],
                                    "custom_attachmentsppc": values['aattachmentppc_' + serial],
                                    "warranty_expiry_date": values['warranty_expiry_date_' + serial],
                                    "amc_expiry_date": values['amc_expiry_date_' + serial]
                                }
                            );
                        });
                        dialog.hide();
                    }
                });

                dialog.show();
            }
        });
    }
});
