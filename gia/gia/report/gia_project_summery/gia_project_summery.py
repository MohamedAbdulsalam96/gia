# Copyright (c) 2013, Ahmed Mohammed Alkuhlani and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	if not filters: filters = {}
	
	columns = get_columns()
	data = get_employees(filters)

	return columns, data

def get_columns():
	return [
		_("GIA Project") + ":Link/GIA Project:100",
		_("Project Name") + ":Data:200",
		_("Sector Name") + ":Data:100",
		_("Sub Sector Name") + ":Data:100",
		_("Products & Annual Production Capacity") + ":Data:50",
		_("Estimated Investment Costs") + ":Data:50",
		_("GIA Project Equipment") + ":Data:50",
		_("GIA Project Requirement") + ":Data:50",
		_("GIA Project Services") + ":Data:50",
		_("GIA Project Staff") + ":Data:50",
		_("GIA Project Location") + ":Data:50",
		_("GIA Project Land Section") + ":Data:50",
		_("GIA Project Land Availability") + ":Data:50"
	]

def get_employees(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select name, project_name, sector_name, sub_sector_name, (select IFNULL(count(*),0) from `tabGIA Project PAPC` where parent=pro.name)
	,(select IFNULL(count(*),0) from `tabGIA Project EIC` where parent=pro.name)
	,(select IFNULL(count(*),0) from `tabGIA Project Equipment` where parent=pro.name)
	,(select IFNULL(count(*),0) from `tabGIA Project Requirement` where parent=pro.name)
	,(select IFNULL(count(*),0) from `tabGIA Project Service` where parent=pro.name)
	,(select IFNULL(count(*),0) from `tabGIA Project Staff` where parent=pro.name)
	,(select IFNULL(count(*),0) from `tabGIA Project Location` where parent=pro.name)
	,(select IFNULL(count(*),0) from `tabGIA Project Land` where parent=pro.name)
	,(select IFNULL(count(*),0) from `tabGIA Project Land Availability` where parent=pro.name)
	from `tabGIA Project` pro {conditions}""".format(
			conditions=get_conditions(filters),
		),
		filters, as_list=1)


def get_conditions(filters):
	conditions = []
	if filters.get("sector"): conditions.append("gia_sector = %(sector)s")
	if filters.get("project"): conditions.append("name = %(project)s")
	return "where {}".format(" and ".join(conditions)) if conditions else ""