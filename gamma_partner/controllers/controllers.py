# -*- coding: utf-8 -*-
# from odoo import http


# class GammaPartner(http.Controller):
#     @http.route('/gamma_partner/gamma_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gamma_partner/gamma_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gamma_partner.listing', {
#             'root': '/gamma_partner/gamma_partner',
#             'objects': http.request.env['gamma_partner.gamma_partner'].search([]),
#         })

#     @http.route('/gamma_partner/gamma_partner/objects/<model("gamma_partner.gamma_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gamma_partner.object', {
#             'object': obj
#         })
