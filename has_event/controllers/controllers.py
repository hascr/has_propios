# -*- coding: utf-8 -*-
# from odoo import http


# class HasEvent(http.Controller):
#     @http.route('/has_event/has_event', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/has_event/has_event/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('has_event.listing', {
#             'root': '/has_event/has_event',
#             'objects': http.request.env['has_event.has_event'].search([]),
#         })

#     @http.route('/has_event/has_event/objects/<model("has_event.has_event"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('has_event.object', {
#             'object': obj
#         })
