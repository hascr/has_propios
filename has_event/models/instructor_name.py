# -*- coding: utf-8 -*-

from odoo import models, fields, api


class instructorname(models.Model):
    _name = 'instructor.name'
    _description = 'Nombre instructor'

    name = fields.Char(string='Instructor')
    sharepoint_id = fields.Integer(string='Id de SharePoint')
