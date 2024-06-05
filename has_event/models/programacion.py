# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Programacion(models.Model):
    _name = 'programacion'
    _description = _('Programacion de sesiones de entrenamiento')
    _rec_name = 'cod_nombre'

    codigo = fields.Char(string="Código")
    curso = fields.Char(string="Curso")
    cuenta = fields.Char(string="Cuenta", compute='_compute_cuenta')
    inicio = fields.Datetime(string="Inicio")
    fin = fields.Datetime(string="Fin")
    u_clase = fields.Boolean(string="Última clase")

    cod_nombre = fields.Char(string='N. Curso', compute='_computeVar')
    instructor = fields.Char(string='Instructor', compute='_compute_instructor')
    matricula = fields.Char(string='URL matrícula', compute='_compute_urlmatricula')

    @api.depends('codigo', 'curso')
    def _computeVar(self):
        for line in self:
            line.cod_nombre = f"{line.codigo} - {line.curso}"

    @api.depends('codigo')
    def _compute_instructor(self):
        for record in self:
            # Search for cursos records with matching codigo in the id field
            curso_record = self.env['cursos'].search([('id', '=', record.codigo)])
            if curso_record:
                record.instructor = curso_record.instructor  # Update instructor
            else:
                record.instructor = ''  # Set empty string if no match
    
    """ @api.depends('curso')
    def _compute_curso(self):
        for record in self:
            # Search for cursos records with matching codigo in the id field
            curso_record = self.env['cursos'].search([('id', '=', record.codigo)])
            if curso_record:
                record.curso = curso_record.curso  # Update instructor
            else:
                record.curso = ''  # Set empty string if no match """

    @api.depends('codigo')
    def _compute_cuenta(self):
        for record in self:
            # Search for cursos records with matching codigo in the id field
            curso_record = self.env['cursos'].search([('id', '=', record.codigo)])
            if curso_record:
                record.cuenta = curso_record.goto  # Update instructor
            else:
                record.cuenta = ''  # Set empty string if no match

    @api.depends('codigo')
    def _compute_urlmatricula(self):
        for record in self:
            # Search for cursos records with matching codigo in the id field
            curso_record = self.env['cursos'].search([('id', '=', record.codigo)])
            if curso_record:
                record.matricula = curso_record.matricula  # Update matricula
            else:
                record.matricula = ''  # Set empty string if no match

    def write(self, vals):
        res = super(Programacion, self).write(vals)
        return res
    
    def go_to_event_programacion(self):
        name_form = _('Cursos')
        return {
        'name': name_form,
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'event.event',
        'res_id': int(self.codigo),  # Reference to the other model
        'target': 'new',
        'view_id': self.env.ref(
            'event.view_event_form').id,
        'context': {} # Optional
            }
