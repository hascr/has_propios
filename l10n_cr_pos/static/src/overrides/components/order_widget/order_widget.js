/** @odoo-module */

import { OrderWidget } from "@point_of_sale/app/generic_components/order_widget/order_widget";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

patch(OrderWidget, {
    props: {
        ...OrderWidget.props,
        card_clicked: { type: Boolean, optional: true },
        dev_tax: { type: String, optional: true },
    },
});