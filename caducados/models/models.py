# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class StockMoveLine(models.Model):
	_inherit = "stock.move.line"

	lot_id = fields.Many2one('stock.lot', 'Lot/Serial Number', domain="[('product_id', '=', product_id), ('company_id', '=', company_id), ('expiration_date', '>', datetime.datetime.now())]", check_company=True)

