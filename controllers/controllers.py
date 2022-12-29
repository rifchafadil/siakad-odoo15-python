# -*- coding: utf-8 -*-
# from odoo import http


# class Rifcha(http.Controller):
#     @http.route('/rifcha/rifcha', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rifcha/rifcha/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rifcha.listing', {
#             'root': '/rifcha/rifcha',
#             'objects': http.request.env['rifcha.rifcha'].search([]),
#         })

#     @http.route('/rifcha/rifcha/objects/<model("rifcha.rifcha"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rifcha.object', {
#             'object': obj
#         })
