from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("GIA"),
			"items": [
				{
					"type": "doctype",
					"name": "GIA Sector",
					"description":_("GIA Sector"),
					"onboard": 1
				},
				{
					"type": "doctype",
					"name": "GIA Sub Sector",
					"description":_("GIA Sub Sector"),
					"onboard": 1
				},
				{
					"type": "doctype",
					"name": "GIA Project",
					"description":_("GIA Project"),
					"onboard": 1

				}
			]
		}
	]