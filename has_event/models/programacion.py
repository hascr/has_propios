# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Programacion(models.Model):
    _name = 'programacion'
    _description = _('Programacion de sesiones de entrenamiento')

    codigo = fields.Char(string="Código")
    curso = fields.Char(string="Curso")
    cuenta = fields.Char(string="Cuenta")
    inicio = fields.Datetime(string="Inicio")
    fin = fields.Datetime(string="Fin")