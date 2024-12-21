# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Hr_leave(models.Model):
    _inherit = 'hr.leave'

    signature = fields.Binary('Firma colaborador')
