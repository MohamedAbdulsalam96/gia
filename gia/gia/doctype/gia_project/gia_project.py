# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ahmed Mohammed Alkuhlani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import money_in_words

class GIAProject(Document):
	def validate(self):
		self.currency='USD'
		if self.eic:
			tot=0.0
			for co in self.get("eic"):
				tot+=co.cost
			self.total_cost=tot
			self.total_cost_word = money_in_words(self.total_cost, self.currency)		
		else:
			self.total_cost=0.0
			self.total_cost_word = None
			
		if self.equipment:
			tot=0.0
			for co in self.get("equipment"):
				tot+=co.cost
			self.total_equipment=tot
			self.total_equipment_word = money_in_words(self.total_equipment, self.currency)
		else:
			self.total_equipment=0.0
			self.total_equipment_word = None

		if self.staff:
			tot=0.0
			for co in self.get("staff"):
				tot+=co.qty
			self.total_staff=tot
		else:
			self.total_staff=0
