// /** @odoo-module */
//
// import { PartnerListScreen } from "@point_of_sale/app/screens/partner_list/partner_list";
// import { patch } from "@web/core/utils/patch";
//
// patch(PartnerListScreen.prototype, {
//     createPartner() {
//         super.createPartner(...arguments);
//         this.state.editModeProps.partner.identification_id = [
//             this.pos.identification_id[0].id,
//             this.pos.identification_id[0].name,
//         ];
//     },
// });
