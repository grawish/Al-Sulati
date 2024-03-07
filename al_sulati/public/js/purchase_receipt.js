frappe.ui.form.on("Purchase Receipt", {
    onload: (frm) => {
        console.log('load')
    },
    refresh: (frm) => {
        console.log('refresh')
    },
    on_submit: (frm) => {
        frappe.call({
            method: "al_sulati.al_sulati.doc_events.purchase_receipt.get_all_serials",
            args: {
                name: frm.doc.name
            },
            callback: (data) => {
                serials = data.message
                d = new frappe.ui.Dialog({
                    title: __("Serials Attachment"),
                    fields: [
                        ...serials.map((serial) => {
                            return {
                                label: "Serial No",
                                fieldtype: "Read Only",
                                fieldname: "serial_no_" + serial,
                                default: serial
                            }
                        }),
                        {
                            fieldname: "column_break",
                            fieldtype: "Column Break",
                        },
                        ...serials.map((serial) => {
                            return {
                                label: "Attachment",
                                fieldtype: "Attach",
                                fieldname: "attach_" + serial,
                            }
                        }),
                    ],
                    primary_action_label: "Save",
                    primary_action: async (data) => {
                        for (const serial of serials) {
                            frappe.db.set_value("Serial No", serial, "custom_attachments", data['attach_' + serial])
                        }
                    }
                })
                d.show()
            }
        })
    }
})
