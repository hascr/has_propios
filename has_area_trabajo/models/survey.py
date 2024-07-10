# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class survey(models.Model):
    _name = 'area.survey'
    _auto = False
    _description = 'Area para evaluciones'

    name = fields.Char(
        string='Área de trabajo')

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW area_survey AS (
            SELECT 	a.id AS id,
			a.area AS name

FROM		area_trabajo a
                         );
            """)