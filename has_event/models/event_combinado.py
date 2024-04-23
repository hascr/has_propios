# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class eventcombinado(models.Model):
    _name = 'event.combinado'
    _auto = False
    _description = 'Evento combinado'

    name = fields.Char(
        string='Nombre combinado'
    )
    


    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW event_combinado AS (
            SELECT		e.id as id,
			concat(e.id,' - ',e.name ->> 'es_CR') as name

FROM		event_event e

WHERE		e.stage_id = 3);
            """)