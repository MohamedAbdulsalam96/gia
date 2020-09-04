// Copyright (c) 2016, Ahmed Mohammed Alkuhlani and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["GIA Project Summery"] = {
	"filters": [
	        	{
		            fieldname: 'project',
		            label: __('GIA Project'),
		            fieldtype: 'Link',
		            options: 'GIA Project'        
			},
	        	{
		            fieldname: 'sector',
		            label: __('GIA Sector'),
		            fieldtype: 'Link',
		            options: 'GIA Sector'        
			}
	]
};
