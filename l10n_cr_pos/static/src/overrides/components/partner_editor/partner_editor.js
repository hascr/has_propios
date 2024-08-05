/** @odoo-module */

import { PartnerDetailsEdit } from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import { patch } from "@web/core/utils/patch";

patch(PartnerDetailsEdit.prototype, {
    setup() {
        super.setup(...arguments);
        if (this.pos.isCRCompany()) {
            this.intFields.push("identification_id");
            this.changes.identification_id =
                this.props.partner.identification_id &&
                this.props.partner.identification_id[0];
        }
    },
});
