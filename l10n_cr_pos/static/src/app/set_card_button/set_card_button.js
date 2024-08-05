/** @odoo-module */

import {ProductScreen} from "@point_of_sale/app/screens/product_screen/product_screen";
import {usePos} from "@point_of_sale/app/store/pos_hook";
import {Component} from "@odoo/owl";

export class SetCardButton extends Component {
    static template = "l10n_cr_pos.SetCardButton";

    setup() {
        this.pos = usePos();
    }

    async click() {
        if (typeof this.pos.selectedOrder.card_clicked === 'undefined') {
            this.pos.selectedOrder.card_clicked = false;  // O true, según tu preferencia
        }
       this.pos.selectedOrder.card_clicked = !this.pos.selectedOrder.card_clicked;
        this.pos.selectedOrder.update_dev_tax(this.pos.selectedOrder.card_clicked);
        // alert("SaleOrderManagementScreen");
    }
}

ProductScreen.addControlButton({component: SetCardButton});
