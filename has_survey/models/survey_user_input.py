# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    asesor = fields.Char(string="Asesor", compute='_compute_asesor',store=True)
    asesor_correo = fields.Char(string="Correo", compute='_compute_asesor_correo',store=True)

    @api.depends('survey_id')
    def _compute_asesor(self):
        for record in self:
            curso_record = self.env['surveyasesor'].search([('survey_id', '=',int(record.survey_id.id)),('id', '=', record.id)])
            if curso_record:
                record.asesor =  curso_record.asesor
            else:
                record.asesor = ''

    @api.depends('asesor')
    def _compute_asesor_correo(self):
        for record in self:
            curso_record = self.env['res.partner'].search([('name', '=',record.asesor)])
            if curso_record:
                record.asesor_correo =  curso_record.email
            else:
                record.asesor_correo = ''

class surveyasesor(models.Model):
    _name = 'surveyasesor'
    _auto = False
    _description = 'Vista de asesores asignados a encuestas'

    survey_id = fields.Integer(
        string='Código de encuesta'
    )
    asesor = fields.Char(
        string=''
    )


    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW surveyasesor AS (
            SELECT		s.id as id,
                         --s.id as user_input_id,
				s.survey_id,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id IN ((SELECT sq.id FROM survey_question sq WHERE sq.title->> 'es_CR' ILIKE '%asesor%'))) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS asesor

FROM			survey_user_input s

WHERE			s.STATE = 'done'
AND 			(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id IN ((SELECT sq.id FROM survey_question sq WHERE sq.title->> 'es_CR' ILIKE '%asesor%'))) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) IS NOT null
                         );
            """)