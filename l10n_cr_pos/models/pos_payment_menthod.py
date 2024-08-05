# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    is_credit_card = fields.Boolean('Tarjeta de Crédito?')

