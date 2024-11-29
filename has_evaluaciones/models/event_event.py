# -*- coding: utf-8 -*-

from odoo import models, fields

class Event(models.Model):
    _inherit = "event.event"

    link_eval = fields.Char(
        string="Link evaluación",
        compute="_compute_link_eval",
        readonly=True,  # Prevent accidental modification
        help="Agregue al final &asid=7 para Nancy y &asid=8 para Ricardo",
    )

    #@api.depends("event_type_id", "presencial")
    def _compute_link_eval(self):
        for record in self:
            event_type_id = record.event_type_id
            presencial = record.presencial

            base_urls = {
                (
                    1,
                    False,
                ): "https://form.jotform.com/243135072740045",  # Virtual, Type 1
                (
                    1,
                    True,
                ): "https://form.jotform.com/243147641043955",  # In-Person, Type 1
                (
                    2,
                    False,
                ): "https://form.jotform.com/243155494853969",  # Virtual, Type 2 (example)
                # Add more URL mappings for other event types and modalities here
            }

            key = (event_type_id.id, presencial)  # Use `id` for foreign key comparison
            base_url = base_urls.get(key)

            """ if not base_url:
                raise UserError(
                    "No se ha configurado una URL para el tipo de evento "
                    f"({event_type_id.name}) y modalidad seleccionada."
                ) """

            url = f"{base_url}?cid={record.id}"
            record.link_eval = url

