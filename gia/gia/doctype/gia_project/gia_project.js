// Copyright (c) 2020, Ahmed Mohammed Alkuhlani and contributors
// For license information, please see license.txt

frappe.ui.form.on('GIA Project', {
	// refresh: function(frm) {

	// }
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
