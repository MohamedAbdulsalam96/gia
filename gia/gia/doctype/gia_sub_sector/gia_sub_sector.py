# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ahmed Mohammed Alkuhlani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import json

import frappe
from frappe import _, throw
from frappe.utils import add_days, cstr, date_diff, get_link_to_form, getdate
from frappe.utils.nestedset import NestedSet
from frappe.desk.form.assign_to import close_all_assignments, clear
from frappe.utils import date_diff

class CircularReferenceError(frappe.ValidationError): pass
class EndDateCannotBeGreaterThanProjectEndDateError(frappe.ValidationError): pass

class GIASubSector(NestedSet):
	nsm_parent_field = 'parent_gia_sub_sector'
	def validate(self):
		if not self.gia_sector:
			frappe.throw(_("Please enter the Sector"))

	

def populate_depends_on(self):
		if self.parent_gia_sub_sector:
			parent = frappe.get_doc('GIA Sub Sector', self.parent_gia_sub_sector)
			if not self.name in [row.gia_sub_sector for row in parent.depends_on]:
				parent.append("depends_on", {
					"doctype": "GIA Sub Sector Depends On",
					"gia_sub_sector": self.name,
					"subject": self.subject
				})
				parent.save()

@frappe.whitelist()
def check_if_child_exists(name):
	child_gia_sub_sectors= frappe.get_all("GIA Sub Sector", filters={"parent_gia_sub_sector": name})
	child_gia_sub_sectors= [get_link_to_form("GIA Sub Sector", gia_sub_sector.name) for gia_sub_sector in child_gia_sub_sectors]
	return child_gia_sub_sectors


 
@frappe.whitelist()
def get_children(doctype, parent, gia_sub_sector=None, gia_sector=None, is_root=False):

	filters = [['docstatus', '<', '2']]

	if gia_sub_sector:
		filters.append(['parent_gia_sub_sector', '=', gia_sub_sector])
	elif parent and not is_root:
		# via expand child
		filters.append(['parent_gia_sub_sector', '=', parent])
	else:
		filters.append(['ifnull(`parent_gia_sub_sector`, "")', '=', ''])

	if gia_sector:
		filters.append(['gia_sector', '=', gia_sector])

	gia_sub_sectors= frappe.get_list(doctype, fields=[
		'name as value',
		'subject as title',
		'is_group as expandable'
	], filters=filters, order_by='name')

	# return gia_sub_sectors
	return gia_sub_sectors

@frappe.whitelist()
def add_node():
	from frappe.desk.treeview import make_tree_args
	args = frappe.form_dict
	args.update({
		"name_field": "subject"
	})
	args = make_tree_args(**args)

	if args.parent_gia_sub_sector == 'All GIA Sub Sector' or args.parent_gia_sub_sector == args.gia_sector:
		args.parent_gia_sub_sector = None

	frappe.get_doc(args).insert()

@frappe.whitelist()
def add_multiple_gia_sub_sector(data, parent):
	data = json.loads(data)
	new_doc = {'doctype': 'GIA Sub Sector', 'parent_gia_sub_sector': parent if parent!="All GIA Sub Sector" else ""}
	new_doc['gia_sector'] = frappe.db.get_value('GIA Sub Sector', {"name": parent}, 'gia_sector') or ""

	for d in data:
		if not d.get("gia_sub_sector"): continue
		new_doc['gia_sub_sector'] = d.get("gia_sub_sector")
		new_gia_sub_sector = frappe.get_doc(new_doc)
		new_gia_sub_sector.insert()
