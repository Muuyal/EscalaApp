# -*- coding: utf-8 -*-
from odoo import http

# class EscalaApp(http.Controller):
#     @http.route('/escala_app/escala_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escala_app/escala_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('escala_app.listing', {
#             'root': '/escala_app/escala_app',
#             'objects': http.request.env['escala_app.escala_app'].search([]),
#         })

#     @http.route('/escala_app/escala_app/objects/<model("escala_app.escala_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escala_app.object', {
#             'object': obj
#         })