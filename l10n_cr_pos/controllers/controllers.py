# -*- coding: utf-8 -*-
# from odoo import http


# class .\dewcom\l10nCrPos(http.Controller):
#     @http.route('/.\dewcom\l10n_cr_pos/.\dewcom\l10n_cr_pos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/.\dewcom\l10n_cr_pos/.\dewcom\l10n_cr_pos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('.\dewcom\l10n_cr_pos.listing', {
#             'root': '/.\dewcom\l10n_cr_pos/.\dewcom\l10n_cr_pos',
#             'objects': http.request.env['.\dewcom\l10n_cr_pos..\dewcom\l10n_cr_pos'].search([]),
#         })

#     @http.route('/.\dewcom\l10n_cr_pos/.\dewcom\l10n_cr_pos/objects/<model(".\dewcom\l10n_cr_pos..\dewcom\l10n_cr_pos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('.\dewcom\l10n_cr_pos.object', {
#             'object': obj
#         })

