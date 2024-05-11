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
    cuenta = fields.Char(string="Cuenta")
    inicio = fields.Datetime(string="Inicio")
    fin = fields.Datetime(string="Fin")
    u_clase = fields.Boolean(string="Última clase")

    cod_nombre = fields.Char(string='N. Curso', compute='_computeVar')


    @api.depends('codigo', 'curso')
    def _computeVar(self):
        for line in self:
            line.cod_nombre = f"{line.codigo} - {line.curso}"