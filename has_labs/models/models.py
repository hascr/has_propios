# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class has_labs(models.Model):
#     _name = 'has_labs.has_labs'
#     _description = 'has_labs.has_labs'


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    lab_canc = fields.Boolean(
        string='Lab. Canc.'
    )



class labsreport(models.Model):
    _name = 'labs.report'
    _auto = False
    _description = 'Reporte Laboratorios'

    fecha = fields.Date(
        string='Fecha'
    )
    pedido = fields.Char(
        string='Número de factura'
    )
    laboratorio = fields.Char(
        string='Examen realizado'
    )
    mascota = fields.Char(
        string='Mascota'
    )
    qty = fields.Float(
        string='Qty'
    )
    precio_unit = fields.Float(
        string='P/U'
    )
    lab_canc = fields.Boolean (
        default=False, string='Lab. Canc.'
    )
    
    subtotal = fields.Float(string='Subtotal', compute='_computeVar')
    
    @api.depends('qty', 'precio_unit')
    def _computeVar(self):
        for line in self:
            line.subtotal = line.qty * line.precio_unit
    
    
    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW labs_report AS (
            SELECT 	    
                        POL.id AS id,
                        cast(POL.create_date as date) as fecha,
			            PO.name as pedido,
			            PT.name as laboratorio,
			            POL.customer_note as mascota,
			            POL.qty as qty, 
			            ROUND(POL.price_subtotal/NULLIF(qty, 0),2) as precio_unit,
                        POL.lab_canc as lab_canc

            FROM		pos_order_line POL
            JOIN 		product_product PP ON PP.id = POL.product_id
            JOIN		product_template PT ON PT.id = PP.product_tmpl_id
            JOIN		pos_category PC ON PC.id = PT.pos_categ_id
            JOIN		pos_order PO ON PO.id = POL.order_id
			
            --WHERE 	DATE(POL.create_date) >= DATE(now())-360
            WHERE		PC.id = 5

            ORDER BY	FECHA ASC
            );
            
            CREATE OR REPLACE RULE update_labs_report AS
                ON UPDATE TO labs_report
                DO INSTEAD
                UPDATE pos_order_line SET lab_canc = new.lab_canc
                WHERE pos_order_line.id = old.id;
                
            CREATE OR REPLACE RULE update_labs_mascota AS
                ON UPDATE TO labs_report
                DO INSTEAD
                UPDATE pos_order_line SET customer_note = new.mascota
                WHERE pos_order_line.id = old.id;
            """)