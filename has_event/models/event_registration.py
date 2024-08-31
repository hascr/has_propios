# -*- coding: utf-8 -*-

from odoo import models, fields, api


class has_eventregistration(models.Model):
    _inherit = "event.registration"

    cedula = fields.Char(string="Cédula")
    placa = fields.Char(string="Placa")
    colaborador = fields.Char(string="N° Colaborador")
    correo = fields.Char(string="Correo personal")
    licencia = fields.Char(string="Licencia")
    asistencia = fields.Float(string="Horas asistidas")
    nota = fields.Float(string="Nota obtenida")
    asesor = fields.Many2one(
        comodel_name="res.users",
        tracking=True,
        string="Asesor",
        domain=lambda self: [
            ("groups_id", "=", self.env.ref("sales_team.group_sale_salesman").id)
        ],
    )
    country_id = fields.Many2one(
        comodel_name="res.country", tracking=True, string="País"
    )
    celular = fields.Char(string="Celular")
    puesto = fields.Char(string="Puesto")

    total_horas_from_event = fields.Float(
        string="Total horas", compute="_compute_float_field"
    )

    @api.depends("event_id")
    def _compute_float_field(self):
        for record in self:
            if record.event_id:
                record.total_horas_from_event = record.event_id.total_horas
            else:
                record.total_horas_from_event = 0.0

    cumple = fields.Char(compute="_compute_total_amount", string="Estado", store=True)

    @api.depends("total_horas_from_event", "asistencia")
    def _compute_total_amount(self):
        for record in self:
            if record.total_horas_from_event == 0 or record.asistencia == 0:
                record.cumple = "No cumple"  # Handle division by zero
            else:
                if record.asistencia / record.total_horas_from_event >= 0.80:
                    record.cumple = "Aprobado"
                else:
                    record.cumple = "Reprobado"