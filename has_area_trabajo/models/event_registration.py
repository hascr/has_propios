# -*- coding: utf-8 -*-

from odoo import models, fields, api


class event_registration(models.Model):
    _inherit = 'event.registration'

    area_id = fields.Many2one(comodel_name='area.trabajo', string='Area de trabajo')