# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_order(models.Model):
    _inherit = 'sale.order'

    asesor_comp = fields.Many2many(comodel_name='res.users', tracking=True, string='Asesor compartido', domain=lambda self: [("groups_id", "=", self.env.ref( "sales_team.group_sale_salesman" ).id)])