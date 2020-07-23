frappe.provide("frappe.treeview_settings");

frappe.treeview_settings['GIA Sub Sector'] = {
	get_tree_nodes: "gia.gia.doctype.gia_sub_sector.gia_sub_sector.get_children",
	add_tree_node:  "gia.gia.doctype.gia_sub_sector.gia_sub_sector.add_node",
	filters: [
		{
			fieldname: "gia_sector",
			fieldtype:"Link",
			options: "GIA Sector",
			label: __("GIA Sector"),
		},
		{
			fieldname: "gia_sub_sector",
			fieldtype:"Link",
			options: "GIA Sub Sector",
			label: __("GIA Sub Sector"),
			get_query: function() {
				var me = frappe.treeview_settings['GIA Sub Sector'];
				var gia_sector= me.page.fields_dict.gia_sector.get_value();
				var args = [["GIA Sub Sector", 'is_group', '=', 1]];
				if(gia_sector){
					args.push(["GIA Sub Sector", 'gia_sector', "=", gia_sector]);
				}
				return {
					filters: args
				};
			}
		}
	],
	breadcrumb: "GIA Sectors",
	get_tree_root: false,
	root_label: "All GIA Sub Sector",
	ignore_fields: ["parent_gia_sub_sector"],
	onload: function(me) {
		frappe.treeview_settings['GIA Sub Sector'].page = {};
		$.extend(frappe.treeview_settings['GIA Sub Sector'].page, me.page);
		me.make_tree();
	},
	toolbar: [
		{
			label:__("Add Multiple"),
			condition: function(node) {
				return node.expandable;
			},
			click: function(node) {
				this.data = [];
				const dialog = new frappe.ui.Dialog({
					title: __("Add Multiple GIA Sub Sector"),
					fields: [
						{
							fieldname: "multiple_gia_sub_sector", fieldtype: "Table",
							in_place_edit: true, data: this.data,
							get_data: () => {
								return this.data;
							},
							fields: [{
								fieldtype:'Data',
								fieldname:"subject",
								in_list_view: 1,
								reqd: 1,
								label: __("GIA Sub Sector")
							}]
						},
					],
					primary_action: function() {
						dialog.hide();
						return frappe.call({
							method: "gia.gia.doctype.gia_sub_sector.gia_sub_sector.add_multiple_gia_sub_sector",
							args: {
								data: dialog.get_values()["multiple_gia_sub_sector"],
								parent: node.data.value
							},
							callback: function() { }
						});
					},
					primary_action_label: __('Create')
				});
				dialog.show();
			}
		}
	],
	extend_toolbar: true
};