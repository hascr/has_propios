# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    area_id = fields.Many2one(comodel_name='area.trabajo', string='Area de trabajo')