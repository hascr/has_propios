/** @odoo-module */

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

patch(PaymentScreen.prototype, {
    // async _isOrderValid(isForceValidate) {
    //     if (this.pos.isEcuadorianCompany()) {
    //         if (
    //             this.currentOrder._isRefundOrder() &&
    //             this.currentOrder.get_partner().id === this.pos.finalConsumerId
    //         ) {
    //             this.popup.add(ErrorPopup, {
    //                 title: _t("Refund not possible"),
    //                 body: _t("You cannot refund orders for Consumidor Final."),
    //             });
    //             return false;
    //         }
    //     }
    //     return super._isOrderValid(...arguments);
    // },
    addNewPaymentLine(paymentMethod) {
        if (this.pos.selectedOrder.card_clicked && !paymentMethod.is_credit_card) {
             this.notification.add(_t("No puedes usar este método de pago si se esta aplicando devolución de iva"), 3000);
        }
        else{
            super.addNewPaymentLine(paymentMethod);
        }
    },


    shouldDownloadInvoice() {
        return this.pos.isCRCompany() ? false : super.shouldDownloadInvoice();
    },
});
