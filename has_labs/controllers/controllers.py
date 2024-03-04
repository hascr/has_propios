# -*- coding: utf-8 -*-
# from odoo import http


# class HasLabs(http.Controller):
#     @http.route('/has_labs/has_labs', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/has_labs/has_labs/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('has_labs.listing', {
#             'root': '/has_labs/has_labs',
#             'objects': http.request.env['has_labs.has_labs'].search([]),
#         })

#     @http.route('/has_labs/has_labs/objects/<model("has_labs.has_labs"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('has_labs.object', {
#             'object': obj
#         })
