# Copyright (c) 2024, Hybrowlabs Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
class Machine(Document):
	def before_save(self):
		self.machine_name = f"{self.parent1} {self.machine_code or ''}"


