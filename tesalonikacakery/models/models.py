# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ModelDasar(models.Model):
    _name = 'tesalonikacakery.base'
    _description = 'model dasar tesalonika cakery'
 
    ukuran = fields.Selection(string="Ukuran Kue", selection=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
    rasa = fields.Selection(string="Rasa", selection=[('coklat', 'Coklat'), ('keju','Keju'),
    ('kacang','Kacang')])
    jenis = fields.Selection(string='Jenis Kue', selection=[('brownies','Brownies'),('donat','Donat')])


class tesalonikacakery(models.Model):
    _name = 'tesalonikacakery.kue'
    _description = 'Daftar Kue'
    _inherit = "tesalonikacakery.base"

    name = fields.Char(string='model kue', required=True)
    active = fields.Boolean(default=True)

    models_id = fields.One2many(
    comodel_name='tesalonikacakery.detailkue', 
    inverse_name='stock_id', 
    string='Detail')

    @api.constrains('name')
    def _constrains_name(self):
        for rec in self:
            duplicate = self.env['tesalonikacakery.kue'].search([('name','=',rec.name)])
            if len(duplicate)>1:
                raise ValidationError("Model %s Sudah Ada di Daftar!! %s" % (str(rec.name).upper(),str(len(duplicate))))
 
    @api.onchange('jenis')
    def _onchange_tipe(self):
        if self.type == 'brownies':
            return {
                'warning': {
                    'title' : 'Jenis Kue',
                }
            }
        elif self.type == 'donat':
            return {
                'warning': {
                    'title' : 'Jenis Kue',
                }
            }

