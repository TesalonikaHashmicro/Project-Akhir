# -*- coding: utf-8 -*-
# from odoo import http

from odoo import http
from odoo.http import request
 
import json
 
 
class ModelDasar(http.Controller):
    @http.route('/kue', auth='public')
    def index(self, **kw):
        model = request.env['tesalonikacakery.kue'].search([])
        value = []
        for data in model:
            value.append({
                'nama':data.name,
                'ukuran':data.ukuran,
                'rasa':data.rasa,
                'jenis':data.jenis
            })

        return json.dumps(value)
   
    @http.route('/detailkue', auth='public')
    def index1(self, **kw):
        model = request.env['tesalonikacakery.detailkue'].search([])
        value = []
        for data in model:
            value.append({
                'teknik':data.teknik,
                'harga':data.harga,
                'potongan':data.potongan
            })
        return json.dumps(value)



# class TesalonikaCakery(http.Controller):
#     @http.route('/tesalonika_cakery/tesalonika_cakery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tesalonika_cakery/tesalonika_cakery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tesalonika_cakery.listing', {
#             'root': '/tesalonika_cakery/tesalonika_cakery',
#             'objects': http.request.env['tesalonika_cakery.tesalonika_cakery'].search([]),
#         })

#     @http.route('/tesalonika_cakery/tesalonika_cakery/objects/<model("tesalonika_cakery.tesalonika_cakery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tesalonika_cakery.object', {
#             'object': obj
#         })

