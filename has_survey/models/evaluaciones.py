# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Evaluaciones(models.Model):
    _name = 'evaluaciones'
    _description = _('Evaluaciones')

    name = fields.Char(_('Participante'))
    fecha_evaluacion = fields.Datetime(_('Realizada'))
    nota = fields.Float(_('Nota'))
    enviar_info = fields.Char(_('Enviar Información'))
    curso = fields.Char(_('Curso'))
    asesor = fields.Char(_('Asesor'))
    intereses = fields.Char(_('Intereses'))
    correo_interes = fields.Char(_('Correo Interés'))
    empresa = fields.Char(_('Empresa'))
    whatsapp = fields.Char(_('WhatsApp'))
    Comentarios = fields.Text(_('Comentarios'))
    correo = fields.Char(_('Correo Contacto'))
    telefono = fields.Char(_('Teléfono'))
    instructor = fields.Char(_('Instructor'))
    duracion = fields.Float(_('Duración'))


def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW estudiantes AS (
            SELECT 
 		e.id AS id,
		e.name AS nombre,
		concat(date_part('year'::text, e.create_date), to_char(e.create_date, 'MM'::text), '-', e.id) AS codest,
    	btrim((e.email)::text) AS correo,
    	t.id AS codigo,
    	t.name->> 'es_CR' AS curso,
	   t.urlmatricula AS matricula,
   	(SELECT ta.cuenta FROM training_account ta WHERE ta.id = t.cuenta_id) AS cuenta,
    	t.date_begin AS inicio,
    	to_char(t.date_begin, 'yyyy-mm-dd'::text) AS inicio_corto,
    	t.date_end AS final,
    	e.nota AS nota,
    	((t.cantsesion)::numeric * (t.hsesion)::numeric) AS tiempototal,
    	e.asistencia AS horas,
    	(SELECT rp1.email FROM res_partner rp1 JOIN res_users ru1 on ru1.partner_id = rp1.id WHERE ru1.id = e.asesor) AS asesor,
    	e.id AS estudiante,
    	t.presencial AS presencial,
    	t.noenviar AS noenviar,
    	e.licencia AS licencia,
    	t.enofi AS lugar,
    	t.fechas_teams_pres AS fechas,
    	btrim((e.name)::text) AS nombres,
		concat('(',e.id,')') AS apellidos 

   FROM event_registration e
   	JOIN event_event t ON t.id = e.event_id
  	WHERE t.stage_id != 5
	AND e.state != 'cancel');
            """)