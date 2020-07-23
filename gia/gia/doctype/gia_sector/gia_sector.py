# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ahmed Mohammed Alkuhlani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.model.document import Document

class GIASector(Document):
	def validate(self):
		if not self.parent_gia_sector:
			frappe.throw(_("Please enter the parent"))
