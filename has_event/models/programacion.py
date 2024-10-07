# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Programacion(models.Model):
    _name = "programacion"
    _description = _("Programacion de sesiones de entrenamiento")
    _rec_name = "cod_nombre"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    active = fields.Boolean(string="Activo", default=True)
    codigo = fields.Char(string="Código", tracking=True)
    curso = fields.Char(string="Curso", tracking=True)
    cuenta = fields.Char(string="Cuenta ", compute="_compute_cuenta", tracking=True)
    cuenta_nombre = fields.Char(
        string="Cuenta", compute="_compute_cuenta_nombre", tracking=True, store=True
    )
    inicio = fields.Datetime(string="Inicio", tracking=True)
    fin = fields.Datetime(string="Fin", tracking=True)
    u_clase = fields.Boolean(string="Última clase", tracking=True)

    cod_nombre = fields.Char(string="N. Curso", compute="_computeVar", tracking=True)
    instructor = fields.Char(
        string="Instructor", compute="_compute_instructor", tracking=True
    )
    matricula = fields.Char(
        string="URL matrícula", compute="_compute_urlmatricula", tracking=True
    )
    soporte = fields.Many2one(
        comodel_name="hr.employee",
        string="Soporte ",
        compute="_compute_soporte",
        tracking=True,
    )
    soporte_nombre = fields.Char(
        string="Soporte",
        compute="_compute_soporte_nombre",
        tracking=True,
        store=True,
    )

    asistencia = fields.Boolean(string="Asistencia", tracking=True)
    video = fields.Boolean(string="Videos", tracking=True)

    @api.depends("codigo", "curso")
    def _computeVar(self):
        for line in self:
            line.cod_nombre = f"{line.codigo} - {line.curso}"

    @api.depends("codigo")
    def _compute_instructor(self):
        for record in self:
            # Search for cursos records with matching codigo in the id field
            curso_record = self.env["cursos"].search([("id", "=", record.codigo)])
            if curso_record:
                record.instructor = curso_record.instructor  # Update instructor
            else:
                record.instructor = ""  # Set empty string if no match

    @api.depends("codigo")
    def _compute_soporte(self):
        for record in self:
            # Search for cursos records with matching codigo in the id field
            curso_record = self.env["event.event"].search(
                [("id", "=", int(record.codigo))]
            )
            if curso_record:
                record.soporte = curso_record.soporte  # Update instructor
            else:
                record.soporte = ""  # Set empty string if no match

    @api.depends("cuenta")
    def _compute_cuenta_nombre(self):
        for record in self:
            record.cuenta_nombre = record.cuenta

    @api.depends("soporte")
    def _compute_soporte_nombre(self):
        for record in self:
            if record.soporte:
                # Access the employee name through the 'name' field of the related record
                record.soporte_nombre = record.soporte.name
            else:
                record.soporte_nombre = False

    @api.depends("codigo")
    def _compute_cuenta(self):
        for record in self:
            # Search for cursos records with matching codigo in the id field
            curso_record = self.env["cursos"].search([("id", "=", record.codigo)])
            if curso_record:
                record.cuenta = curso_record.goto  # Update instructor
            else:
                record.cuenta = ""  # Set empty string if no match

    @api.depends("codigo")
    def _compute_urlmatricula(self):
        for record in self:
            # Search for cursos records with matching codigo in the id field
            curso_record = self.env["cursos"].search([("id", "=", record.codigo)])
            if curso_record:
                record.matricula = curso_record.matricula  # Update matricula
            else:
                record.matricula = ""  # Set empty string if no match

    def write(self, vals):
        res = super(Programacion, self).write(vals)
        return res

    def go_to_event_programacion(self):
        name_form = _("Cursos")
        return {
            "name": name_form,
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "event.event",
            "res_id": int(self.codigo),  # Reference to the other model
            "target": "current",
            "view_id": self.env.ref("event.view_event_form").id,
            "context": {},  # Optional
        }

    def solicitar_programacion(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://forms.office.com/r/0AVpVrJjDZ",
        }
