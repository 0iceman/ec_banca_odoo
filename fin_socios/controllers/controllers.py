# -*- coding: utf-8 -*-
from odoo import http

# class FinSocios(http.Controller):
#     @http.route('/fin_socios/fin_socios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fin_socios/fin_socios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fin_socios.listing', {
#             'root': '/fin_socios/fin_socios',
#             'objects': http.request.env['fin_socios.fin_socios'].search([]),
#         })

#     @http.route('/fin_socios/fin_socios/objects/<model("fin_socios.fin_socios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fin_socios.object', {
#             'object': obj
#         })