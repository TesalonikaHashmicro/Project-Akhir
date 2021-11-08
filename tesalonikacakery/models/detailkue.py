# -*- coding: utf-8 -*-
 
from odoo import models, fields, api
 
class tesalonikacakery(models.Model):
    _name = 'tesalonikacakery.detailkue'
    _description = 'Daftar Detail Pembuatan Kue'
    
    teknik = fields.Selection(string='Teknik Pembuatan', selection=[('kukus','Kukus'),('panggang','Panggang'),('goreng','Goreng')])
    potongan = fields.Selection(string='Potongan Kue', selection=[('slice','Slice'),('utuh','Utuh'),('satuan','Satuan'),('box','Box')])
    stock = fields.Integer(string='Stock Kue', required=True)
    harga = fields.Integer(string='Harga Kue', required=True)
    pembuatan = fields.Datetime(string='Tanggal Pembuatan', default=fields.Datetime.now)
    expired =  fields.Datetime(string='Tanggal Expired', default=fields.Datetime.now)
    
    tersedia = fields.Boolean(string='tersedia',
                             default=True
    )


    stock_id = fields.Many2one(
    comodel_name='tesalonikacakery.kue', 
    string='Kue', 
    required=True,
    delegate=True)

    pegawai_id = fields.Many2one(comodel_name="res.partner", string="Penanggung Jawab", 
    domain="[('is_pegawainya','ilike',True)]")

    # qty = fields.Integer(compute='_compute_qty', string='qty')
    # kurangistock = fields.Many2many('tesalonikacakery.detailpembelian', string = 'stock berkurang')

    @api.depends('stock_id')
    def _compute_deskrip(self):
        for record in self:
            record.deskrip = record.stock_id.deskripsi

    # @api.depends('stock', 'kurangistock')
    # def _compute_qty(self):
    #    for record in self:
    #         record.stock = record.stock - record.qty 
