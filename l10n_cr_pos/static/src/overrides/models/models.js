/** @odoo-module */

import {Order, Orderline, Payment} from "@point_of_sale/app/store/models";
import {patch} from "@web/core/utils/patch";
import {ErrorPopup} from "@point_of_sale/app/errors/popups/error_popup";
import {_t} from "@web/core/l10n/translation";


patch(Orderline.prototype, {


    getDisplayData() {
        var tax_string = '';
        // this.tax_ids = this.get_taxes();
        var taxes = this.get_taxes();

        if (taxes && taxes.length > 0) {
            var tax_names = [];
            for (const tax of taxes) {
                tax_names.push(tax.name);
            }
            tax_string = tax_names.join(', ');
        }
        return {
            ...super.getDisplayData(),
            get_tax_string: tax_string,
        };
    }
});

patch(Order.prototype, {

    update_dev_tax(is_clicked) {
        if (is_clicked) {
            // alert("print desde order")
            var orderlines = this.orderlines;
            for (var i = 0; i < orderlines.length; i++) {
                var taxes = orderlines[i].get_taxes()
                if (!orderlines[i].tax_ids) {
                    orderlines[i].tax_ids = orderlines[i].get_product().taxes_id;
                }
                for (const tax of taxes) {
                    if (tax.dev_tax_id) {
                        if (!orderlines[i].tax_ids.includes(tax.dev_tax_id[0])) {
                            orderlines[i].tax_ids.push(tax.dev_tax_id[0]);
                        }
                    }
                }
            }
        } else {
            var orderlines = this.orderlines;
            for (var i = 0; i < orderlines.length; i++) {
                var taxes = orderlines[i].get_taxes();
                if (orderlines[i].tax_ids) {
                    for (const tax of taxes) {
                        if (tax.dev_tax_id) {
                            // Eliminar el elemento dev_tax_id del arreglo tax_ids si existe
                            const index = orderlines[i].tax_ids.indexOf(tax.dev_tax_id[0]);
                            if (index > -1) {
                                orderlines[i].tax_ids.splice(index, 1);
                            }
                        }
                    }
                }
            }

        }
    },

    async add_product(product, options) {
        const result = await super.add_product(...arguments);
        if (result.product.taxes_id && !this.pos.selectedOrder.card_clicked) {
            for (const tax of result.product.taxes_id) {
                var tax_object = this.pos.getTaxesByIds([tax])
                if (tax_object[0].dev_tax_id) {
                    // Eliminar el elemento dev_tax_id del arreglo tax_ids si existe
                    const index = result.product.taxes_id.indexOf(tax_object[0].dev_tax_id[0]);
                    if (index > -1) {
                        result.product.taxes_id.splice(index, 1);
                    }
                }
            }
        }
        return result;
    },
});
