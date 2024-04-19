# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class estudiantes(models.Model):
    _name = 'estudiantes'
    _auto = False
    _description = 'Vista de estudiantes'

    nombre = fields.Char(
        string='Nombre de estudiante'
    )
    codest = fields.Integer(
        string='Código de estudiante'
    )
    correo = fields.Char(
        string='Correo'
    )
    codigo = fields.Integer(
        string='Código de curso'
    )
    curso = fields.Char(
        string='Curso'
    )
    matricula = fields.Char(
        string='Matricula'
    )
    cuenta = fields.Char(
        string='Cuenta'
    )
    inicio = fields.Datetime(
        string='Inicio'
    )
    inicio_corto = fields.Date(
        string='Inicio corto'
    )
    final = fields.Datetime(
        string='Final'
    )
    nota = fields.Float(
        string='Nota'
    )
    tiempototal = fields.Float(
        string='Tiempo total'
    )
    horas = fields.Float(
        string='Horas'
    )
    asesor = fields.Char(
        string='Asesor'
    )
    estudiante = fields.Float(
        string='Estudiante'
    )
    presencial = fields.Boolean(
        string='Presencial'
    )
    noenviar = fields.Boolean(
        string='No enviar recordatorios'
    )
    licencia = fields.Char(
        string='Licencia'
    )
    lugar = fields.Char(
        string='Lugar'
    )
    fechas = fields.Char(
        string='Fechas'
    )
    nombres = fields.Char(
        string='Nombres'
    )
    apellidos = fields.Char(
        string='Apellidos'
    )
    


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
    	(SELECT rp1.email FROM res_partner rp1 JOIN res_users ru1 on ru1.partner_id = rp1.id WHERE ru1.id = t.asesor) AS asesor,
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