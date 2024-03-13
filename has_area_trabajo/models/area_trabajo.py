# -*- coding: utf-8 -*-

from odoo import models, fields, api


class has_area_trabajo(models.Model):
     _name = 'area.trabajo'
     _rec_name = 'area'
     _description = 'Área de trabajo'

     area = fields.Char(string="Área de trabajo")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

