// Copyright (c) 2020, Ahmed Mohammed Alkuhlani and contributors
// For license information, please see license.txt

frappe.ui.form.on('GIA Project', {
	refresh: function(frm) {
        	cur_frm.set_query("admin1", "gia_project_location", function(doc, cdt, cdn) {
            		var d = locals[cdt][cdn];
	            	return{
	            		filters: [            		    
	            			['GIA Admin', 'admin_type', '=', 'Governate'],
	            			['GIA Admin', 'is_group', '=', 1]
	            		]
	            	}
		});
        	cur_frm.set_query("admin2", "gia_project_location", function(doc, cdt, cdn) {
            		var d = locals[cdt][cdn];
	            	return{
	            		filters: [            		    
	            			['GIA Admin', 'parent_gia_admin', '=', d.admin1]
	            		]
	            	}
		});
        	cur_frm.set_query("admin3", "gia_project_location", function(doc, cdt, cdn) {
            		var d = locals[cdt][cdn];
	            	return{
	            		filters: [            		    
	            			['GIA Admin', 'parent_gia_admin', '=', d.admin2]
	            		]
	            	}
		});


	},
	onload: function(frm){
		cur_frm.set_value("currency", "USD");

		frm.fields_dict["gia_sub_sector"].get_query = function() {
			return {
				filters: {
					"gia_sector": frm.doc.gia_sector,
					"is_group": 0
				}
			};
		};

	},
	gia_sector: function(frm){
		cur_frm.set_value("gia_sub_sector", "");
		cur_frm.set_value("gia_sub_sector_name", "");

	}

});

frappe.ui.form.on('GIA Project Location', 'admin1', function(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	d.admin2 = "";
	d.admin3 = "";
	frm.refresh_fields();
})
frappe.ui.form.on('GIA Project Location', 'admin2', function(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	d.admin3 = "";
	frm.refresh_fields();
})