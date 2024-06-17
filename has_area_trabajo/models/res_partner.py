# -*- coding: utf-8 -*-

from odoo import models, fields, api


class res_partner(models.Model):
    _inherit = 'res.partner'

    area_id = fields.Many2one(comodel_name='area.trabajo', string='Area de trabajo')
    _sql_constraints = [('email_unique', 'unique(email)', "El correo debe ser único")]