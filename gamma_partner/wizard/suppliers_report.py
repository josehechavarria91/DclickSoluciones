# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SuppliersReportWizard(models.TransientModel):
    _name = 'suppliers.report.wizard'
    _description = 'Products By Supplier Report Wizard'

    supplier_id = fields.Many2one('res.partner', 'Supplier')

    def action_print_report(self):
        suppliers = self.env['res.partner'].search([])
        suppliers_list = []
        for supplier in suppliers:
            if supplier.gamma_products_count > 2:
                supplier_tmp = {
                    'name': supplier.name,
                    'count': supplier.gamma_products_count,
                }
                suppliers_list.append(supplier_tmp)
        data = {
            'suppliers': suppliers_list
        }
        return self.env.ref('gamma_partner.action_report_suppliers').report_action(self, data=data)
        # return {
        #     "type": ""
        # }
