# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class webinars(models.Model):
    _name = 'webinars'
    _auto = False
    _description = _('Webinars')

    fecha_evaluacion = fields.Datetime(_('Realizada'))
    nota = fields.Float(_('Nota'), group_operator='avg')
    enviar_info = fields.Char(_('Enviar Información'))
    curso = fields.Char(_('Curso'))
    fuente = fields.Char(_('Fuente'))
    intereses = fields.Char(_('Intereses'))
    correo_intereses = fields.Char(_('Correo Interés'))
    whatsapp = fields.Char(_('WhatsApp'))
    correo = fields.Char(_('Correo Contacto'))
    instructor = fields.Char(_('Instructor'))
    temas_actualizados = fields.Float(_('Temas actualizados'), group_operator='avg')
    temas_utiles = fields.Float(_('Temas útiles'), group_operator='avg')
    estructura = fields.Float(_('Estructura'), group_operator='avg')
    conocimiento = fields.Float(_('Conocimiento'), group_operator='avg')
    rendimiento = fields.Float(_('Rendimiento'), group_operator='avg')
    area_trabajo = fields.Char(_('Área de trabajo'))

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW webinars AS (
            SELECT		s.id AS id,
				s.end_datetime AS fecha_evaluacion,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 106) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS enviar_info,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 103) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS curso,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 105) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS fuente,
				
				( 	(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 267))::NUMERIC --AS temas_actualizados,
					+
					(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 268))::NUMERIC --AS temas_utiles,
					+
					(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 269))::NUMERIC --AS estructura,
					+
					(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 270))::NUMERIC --AS conocimiento,
					+
					(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 271))::NUMERIC --AS rendimiento,
				) / 5 / 5 * 100 AS nota,
				
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 267))::NUMERIC / 5 * 100 AS temas_actualizados,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 268))::NUMERIC / 5 * 100 AS temas_utiles,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 269))::NUMERIC / 5 * 100 AS estructura,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 270))::NUMERIC / 5 * 100 AS conocimiento,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 104) FROM	survey_user_input_line l WHERE l.user_input_id = s.id AND l.matrix_row_id = 271))::NUMERIC / 5 * 100 AS rendimiento,
				
				(SELECT MAX(l.value_ans_sh_email) filter (WHERE l.question_id = 107) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS correo_intereses,
				(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 110) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS intereses,
				CONCAT((SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 108) FROM	survey_user_input_line l WHERE l.user_input_id = s.id),(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 109) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS WhatsApp,
				(SELECT MAX(l.value_ans_sh_email) filter (WHERE l.question_id = 111) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS correo,
				(SELECT c.instructor FROM cursos c WHERE concat(c.codigo,' - ',c.curso) = (SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 103) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))) AS instructor,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 115) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS area_trabjo


FROM			survey_user_input s

WHERE			s.STATE = 'done'
AND			s.survey_id = 6
                         );
            """)
        
    def go_to_webinars(self):
        name_form = _('Webinars')
        return {
        'name': name_form,
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'survey.user_input',
        'res_id': self.id,  # Reference to the other model
        'target': 'current',
        'view_id': self.env.ref(
            'survey.survey_user_input_view_form').id,
        'context': {} # Optional
            }