# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class GammaPartner(models.Model):
    _inherit = 'res.partner'

    gamma_identifier = fields.Char("Identificador")
    gamma_type = fields.Selection([
        ('tcp', 'TCP'),
        ('mipyme', 'Mipyme'),
        ('estatal', 'Estatal'),
        ('sa', 'Sociedad Anónima'),
        ('otro', 'Otros'),
        ], string='Tipo')
    gamma_supplier = fields.Boolean("Proveedor")
    gamma_products_count = fields.Integer(string="Products count", compute="_compute_products_count")
    gamma_products = fields.One2many('product.supplierinfo', 'name', 'Productos')

    def _compute_products_count(self):
        for rec in self:
            count = self.env['product.supplierinfo'].sudo().search_count([('name', '=', rec.id)])
            rec.gamma_products_count = count

    def action_view_products(self):
        print ("Las cuentas no dejan")
# view = {
#     'type': 'ir.actions.act_window',
#     'name': _('Products'),
#     'res_model': 'product.supplierinfo',
#     'view_mode': 'tree',
#     'target': 'new',
#     'domain': [('name', '=', self.id)]
# }
# return view
