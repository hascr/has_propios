from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    cabys_descripcion = fields.Char(
        string="Descripción Cabys",
        help="Descripción de CABYS del Ministerio de Hacienda",
    )
    cabys_impuesto = fields.Integer(
        string="Impuesto Cabys",
        help="Impuesto de referencia de CABYS del Ministerio de Hacienda",
    )

    # @api.depends
    def get_cabys_info(self, cabys_code):
        endpoint = f"https://api.hacienda.go.cr/fe/cabys?codigo={cabys_code}"
        headers = {
            "Cache-Control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        try:
            response = requests.get(endpoint, headers=headers, verify=False)

            response.raise_for_status()
            data = response.json()
            self.cabys_descripcion = data[0]["descripcion"]
            self.cabys_impuesto = data[0]["impuesto"]
        except requests.exceptions.RequestException as e:
                    _logger.error(f"Error al obtener información de CABYS: {e}")
                    raise UserError("Error al obtener información de CABYS. Verifique el código o revise los logs para más detalles.")
        except (IndexError, KeyError):  # Handle specific JSON parsing errors
            _logger.warning(f"CABYS code '{cabys_code}' not found in response.")
            raise UserError(f"El código CABYS '{cabys_code}' no se encontró. Verifique el código ingresado.")

    @api.model
    def create(self, vals):
        if 'cabys_code' in vals:
            record = super(ProductTemplate, self).create(vals)
            record.get_cabys_info(vals['cabys_code'])
        else:
            record = super(ProductTemplate, self).create(vals)
        return record

    def write(self, vals):
        if 'cabys_code' in vals:
            for record in self:
                record.get_cabys_info(vals['cabys_code'])
        return super(ProductTemplate, self).write(vals)
