# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools
#from odoo.addons.base.models.res_currency import Currency


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    material = fields.Float(
        string='Material'
    )

    consultoria = fields.Boolean(
        string='Pago de Consultoría'
    )

#    company_currency_id = fields.Many2one(
#        comodel_name='res.currency',
#        related='company_id.currency_id',
#        string="Company Currency",
#        readonly=True
#    )
#    amount_signed = fields.Monetary(
#        string='Pago en moneda de la compania',
#        currency_field='company_currency_id',
#        store=True,
#        readonly=True,
#        compute='_compute_amount'
#    )

    ##@api.one
#    @api.depends('currency_id', 'company_id')
#    @api.constrains('currency_id', 'company_id')
#    def _compute_amount(self):
#        amount_signed = self.amount
#        if self.currency_id and self.company_id and self.currency_id != self.company_id.currency_id:
#            currency_id = self.currency_id.with_context(date=self.payment_date)
#            amount_signed = currency_id.compute(self.amount, self.company_id.currency_id)
#        self.amount_signed = amount_signed


class AccountPaymentReport(models.Model):
    _name = 'account.payment.report'
    _auto = False
    _description = 'Reporte gestión cobro'

    payment_date = fields.Date(
        string='Fecha de pago'
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Cliente'
    )
    user_id = fields.Many2one(
        'res.users',
        string='Vendedor',
    )
    amount = fields.Float(
        string='Cobro bruto'
    )
    number_invoice = fields.Char(
        string='Número de factura'
    )
    material = fields.Float(
        string='Material'
    )
#    partner_type = fields.Selection(
#        [
#            ('customer', 'Customer'),
#            ('supplier', 'Vendor')
#        ]
#    )
    amount_untaxed = fields.Float(
        string='Cobro Neto'
    )
    commission = fields.Float(
        string='Comisión'
    )
    retencion = fields.Float(
        string='Retención'
    )
    net_commission = fields.Float(
        string='Comisión neta'
    )

    net_amount_usd = fields.Float(
        string='Cobro neto USD'
    )

    tipo_comision = fields.Char (
        'Tipo de comisión'
    )

#    @api.model_cr
    def init(self):
#        tools.drop_view_if_exists(self._cr, "account_payment_report")
        self._cr.execute("""
            CREATE OR REPLACE VIEW account_payment_report AS (
            SELECT 	a.id AS id,
			m.ref AS number_invoice,
			m.date AS payment_date,
			m.partner_id AS partner_id,
			ROUND(m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ),2) amount,
			ROUND(m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) - CASE WHEN a.material::numeric IS NULL THEN 0 ELSE a.material::numeric END,2) amount_untaxed,
			a.material material,
			(SELECT m1.invoice_user_id FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) AS user_id,

			ROUND(CASE WHEN a.consultoria = TRUE THEN (m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) - CASE WHEN a.material::numeric IS NULL THEN 0 ELSE a.material::numeric END) *0.02 ELSE (m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) - CASE WHEN a.material::numeric IS NULL THEN 0 ELSE a.material::numeric END) *0.04 END,2) commission,
			ROUND(CASE WHEN a.consultoria = TRUE THEN (m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) - CASE WHEN a.material::numeric IS NULL THEN 0 ELSE a.material::numeric END) *0.02 ELSE (m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) - CASE WHEN a.material::numeric IS NULL THEN 0 ELSE a.material::numeric END) *0.04 END * 0.15,2) retencion,
			ROUND(CASE WHEN a.consultoria = TRUE THEN (m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) - CASE WHEN a.material::numeric IS NULL THEN 0 ELSE a.material::numeric END) *0.02 ELSE (m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) - CASE WHEN a.material::numeric IS NULL THEN 0 ELSE a.material::numeric END) *0.04 END * 0.85,2) net_commission,
			
			ROUND(ROUND(m.amount_total_signed * (SELECT m1.amount_untaxed/m1.amount_total FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' ) - CASE WHEN a.material::numeric IS NULL THEN 0 ELSE a.material::numeric END,2) * CASE WHEN (SELECT rate FROM res_currency_rate rcr WHERE rcr.currency_id = 2 AND m.date = rcr.name) IS NULL THEN (SELECT rate FROM res_currency_rate rcr WHERE rcr.currency_id = 2 AND m.date = rcr.name LIMIT 1) ELSE (SELECT rate FROM res_currency_rate rcr WHERE rcr.currency_id = 2 AND m.date = rcr.name) END,2) net_amount_usd,
			CASE WHEN a.consultoria = TRUE THEN 'Consultoría' ELSE 'Capacitación' END tipo_comision

	FROM account_payment a
	JOIN	account_move m ON m.id = a.move_id
		
	WHERE	a.payment_type = 'inbound'
	AND	m.state = 'posted'
            )""")
