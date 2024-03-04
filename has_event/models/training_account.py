# -*- coding: utf-8 -*-

from odoo import models, fields, api


class trainingaccount(models.Model):
    _name = 'training.account'
    _rec_name = 'cuenta'
    _description = 'Cuenta Training'

    cuenta = fields.Char(string='Cuenta Training')
