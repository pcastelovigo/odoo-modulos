# -*- coding: utf-8 -*-

from odoo import models, fields, api


class calcular_edad(models.Model):
	_inherit = 'hr.employee'
	_description = 'calcular_edad.calcular_edad'

	edad = fields.Integer(string="Edad", compute="_compute_edad")

	@api.depends('birthday')
	def _compute_edad(self):
		hoy = fields.Date.today()
		if self.birthday is not False:
			diferencia = hoy - self.birthday
			self.edad = diferencia.days // 365
		else:
			self.edad = False
