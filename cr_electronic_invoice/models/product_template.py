from odoo import models, fields, api


class ProductElectronic(models.Model):
    _inherit = "product.template"

    # ==============================================================================================
    #                                          PRODUCT TEMPLATES
    # ==============================================================================================

    @api.model
    def _default_code_type_id(self):
        code_type_id = self.env["code.type.product"].search(
            [("code", "=", "04")], limit=1
        )
        return code_type_id or False

    commercial_measurement = fields.Char(string="Commercial Unit")
    code_type_id = fields.Many2one(
        comodel_name="code.type.product",
        string="Code Type",
        default=_default_code_type_id,
    )
    tariff_head = fields.Char(
        string="Export Tax rate", help="Tax rate to apply for exporting invoices"
    )
    cabys_code = fields.Char(
        string="CABYS Code",
        help="CABYS code from Ministerio de Hacienda"
    )
    economic_activity_id = fields.Many2one(
        comodel_name="economic.activity",
        string="Economic Activity",
        help="Economic activity code from Ministerio de Hacienda",
    )
    non_tax_deductible = fields.Boolean(
        string="Is Non Tax Deductible",
        help="Indicates if this product is non-tax deductible",
    )
    return_iva = fields.Boolean("Devolución IVA?")
