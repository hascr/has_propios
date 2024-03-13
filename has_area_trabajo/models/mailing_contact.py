# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mailing_contact(models.Model):
    _inherit = 'mailing.contact'

    area_id = fields.Many2one(comodel_name='area.trabajo', string='Area de trabajo')