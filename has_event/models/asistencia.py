# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class asistencia(models.Model):
    _name = 'asistencia'
    _description = _('Asistencia de sesiones de entrenamiento')
    _rec_name = 'nombre'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    codigo = fields.Char(string="Código")
    nombre = fields.Char(string="Nombre completo")
    correo = fields.Char(string="Correo electrónico")
    curso = fields.Char(string="Curso")
    #cuenta = fields.Char(string="Cuenta")
    fecha = fields.Datetime(string="Fecha")
    minutos = fields.Float(string="Minutos conectados")
    horas = fields.Float(string="Horas", compute='_compute_horas', store=True)
    tipo = fields.Char(string="Tipo")
    duplicados = fields.Char(string="revisar duplicados")
    cod_nombre = fields.Char(string='N. Curso')
    
    _sql_constraints = [('duplicados_unique', 'unique(duplicados)', "El códdigo duplicados debe ser único")]

    def go_to_event_asistencia(self):
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
    
    @api.depends('minutos','horas')
    def _compute_horas(self):
        for record in self:
            record.horas = record.minutos / 60 #if record.minutos else 0 # Calculate hours from minutes

    """ def write(self, vals):
        res = super(asistencia, self).write(vals)
        return res """
    
    """ @api.depends('codigo', 'curso')
    def _computeVar(self):
        for line in self:
            line.cod_nombre = f"{line.codigo} - {line.curso}" """