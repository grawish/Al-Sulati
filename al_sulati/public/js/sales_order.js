frappe.ui.form.on("Sales Order", {
onload: (frm) => {
console.log("onload")
    frm.set_query("item_code", "custom_machine_allocation",()=>{
            return {
                filters: [["Item", "name", "in", frm.doc.items.map(i=>i.item_code)]]
            }
        })
},
refresh: (frm) => {
frm.set_query("item_code", "custom_machine_allocation",()=>{
console.log("refresh")
            return {
                filters: [["Item", "name", "in", frm.doc.items.map(i=>i.item_code)]]
            }
        })
},
    items: (frm) => {

        frm.set_query("item_code", "custom_machine_allocation",()=>{
            return {
                filters: [["Item", "name", "in", frm.doc.items.map(i=>i.item_code)]]
            }
        })
    }
})


frappe.ui.form.on("Machine Allocation", "item_code", function(frm, cdt, cdn){
  var child = locals[cdt][cdn];
  var grid_row = cur_frm.fields_dict['custom_machine_allocation'].grid.grid_rows_by_docname[cdn],
       field = frappe.utils.filter_dict(grid_row.docfields, {fieldname: "machine"})[0];

  field.get_query =  function(){
    return {
       filters: { parent1: child.item_code }
  }
  grid_row.refresh_field("machine");
}
});
