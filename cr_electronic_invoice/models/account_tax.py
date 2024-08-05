from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools.misc import formatLang
from collections import defaultdict


class IvaCodeType(models.Model):
    _inherit = "account.tax"

    # ==============================================================================================
    #                                          TAXES
    # ==============================================================================================

    tax_code = fields.Char(
        string="Tax Code"
    )
    iva_tax_desc = fields.Char(
        string="VAT Tax Rate",
        default='N/A'
    )
    iva_tax_code = fields.Char(
        string="VAT Rate Code",
        default='N/A'
    )
    has_exoneration = fields.Boolean(
        string="Has Exoneration"
    )
    percentage_exoneration = fields.Integer(
        string="Percentage of VAT Exoneration"
    )
    tax_root = fields.Many2one(
        comodel_name="account.tax",
        string="Parent Tax"
    )
    non_tax_deductible = fields.Boolean(
        string='Indicates if this tax is no deductible for Rent and VAT'
    )

    dev_tax_id = fields.Many2one('account.tax')

    # -------------------------------------------------------------------------
    # ONCHANGE METHODS
    # -------------------------------------------------------------------------

    @api.onchange('percentage_exoneration')
    def _onchange_percentage_exoneration(self):
        self.tax_compute_exoneration()

    @api.onchange('tax_root')
    def _onchange_tax_root(self):
        self.tax_compute_exoneration()

    def tax_compute_exoneration(self):
        if self.percentage_exoneration <= 13:
            if self.tax_root:
                self.amount = self.tax_root.amount - self.percentage_exoneration
        else:
            raise UserError(_('El porcentaje no puede ser mayor a 13'))

    # @api.model
    # def _prepare_tax_totals(self, base_lines, currency, tax_lines=None):
    #     # ==== Compute the taxes ====
    #
    #     to_process = []
    #     for base_line in base_lines:
    #         to_update_vals, tax_values_list = self._compute_taxes_for_single_line(base_line)
    #         to_process.append((base_line, to_update_vals, tax_values_list))
    #
    #     def grouping_key_generator(base_line, tax_values):
    #         source_tax = tax_values['tax_repartition_line'].tax_id
    #         return {'tax_group': source_tax.tax_group_id}
    #
    #     global_tax_details = self._aggregate_taxes(to_process, grouping_key_generator=grouping_key_generator)
    #
    #     tax_group_vals_list = []
    #     for tax_detail in global_tax_details['tax_details'].values():
    #         tax_group_vals = {
    #             'tax_group': tax_detail['tax_group'],
    #             'base_amount': tax_detail['base_amount_currency'],
    #             'tax_amount': tax_detail['tax_amount_currency'],
    #         }
    #
    #         # Handle a manual edition of tax lines.
    #         if tax_lines is not None:
    #             matched_tax_lines = [
    #                 x
    #                 for x in tax_lines
    #                 if x['tax_repartition_line'].tax_id.tax_group_id == tax_detail['tax_group']
    #             ]
    #             if matched_tax_lines:
    #                 tax_group_vals['tax_amount'] = sum(x['tax_amount'] for x in matched_tax_lines)
    #
    #         tax_group_vals_list.append(tax_group_vals)
    #
    #     tax_group_vals_list = sorted(tax_group_vals_list, key=lambda x: (x['tax_group'].sequence, x['tax_group'].id))
    #
    #     # ==== Partition the tax group values by subtotals ====
    #
    #     amount_untaxed = global_tax_details['base_amount_currency']
    #     amount_tax = 0.0
    #
    #     subtotal_order = {}
    #     groups_by_subtotal = defaultdict(list)
    #     for tax_group_vals in tax_group_vals_list:
    #         tax_group = tax_group_vals['tax_group']
    #
    #         subtotal_title = tax_group.preceding_subtotal or _("Subtotal")
    #         sequence = tax_group.sequence
    #
    #         subtotal_order[subtotal_title] = min(subtotal_order.get(subtotal_title, float('inf')), sequence)
    #         groups_by_subtotal[subtotal_title].append({
    #             'group_key': tax_group.id,
    #             'tax_group_id': tax_group.id,
    #             'tax_group_name': tax_group.name,
    #             'tax_group_amount': tax_group_vals['tax_amount'],
    #             'tax_group_base_amount': tax_group_vals['base_amount'],
    #             'formatted_tax_group_amount': formatLang(self.env, tax_group_vals['tax_amount'], currency_obj=currency),
    #             'formatted_tax_group_base_amount': formatLang(self.env, tax_group_vals['base_amount'],
    #                                                           currency_obj=currency),
    #         })
    #
    #     # ==== Build the final result ====
    #     amount_911_cruz = 0
    #
    #     subtotals = []
    #     amount_911_cruz = 0
    #     for subtotal_title in sorted(subtotal_order.keys(), key=lambda k: subtotal_order[k]):
    #         amount_total = amount_untaxed + amount_tax
    #         subtotals.append({
    #             'name': subtotal_title,
    #             'amount': amount_total,
    #             'formatted_amount': formatLang(self.env, amount_total, currency_obj=currency),
    #         })
    #         amount_911_cruz = 0
    #         # se sobreescribe para incluir el impuesto 911 y cruz roja
    #         for x in groups_by_subtotal[subtotal_title]:
    #             if x['tax_group_amount'] > 0.0:
    #                 amount_tax += x['tax_group_amount']
    #             else:
    #                 amount_tax += x['tax_group_base_amount']
    #                 amount_911_cruz += x['tax_group_base_amount']
    #
    #         # amount_tax += sum(x['tax_group_amount'] for x in groups_by_subtotal[subtotal_title])
    #     amount_total = amount_untaxed + amount_tax - amount_911_cruz
    #
    #     display_tax_base = (len(global_tax_details['tax_details']) == 1 and currency.compare_amounts(
    #         tax_group_vals_list[0]['base_amount'], amount_untaxed) != 0) \
    #                        or len(global_tax_details['tax_details']) > 1
    #
    #     return {
    #         'amount_untaxed': currency.round(amount_untaxed) if currency else amount_untaxed,
    #         'amount_total': currency.round(amount_total) if currency else amount_total,
    #         'formatted_amount_total': formatLang(self.env, amount_total, currency_obj=currency),
    #         'formatted_amount_untaxed': formatLang(self.env, amount_untaxed, currency_obj=currency),
    #         'groups_by_subtotal': groups_by_subtotal,
    #         'subtotals': subtotals,
    #         'subtotals_order': sorted(subtotal_order.keys(), key=lambda k: subtotal_order[k]),
    #         'display_tax_base': display_tax_base,
    #     }
