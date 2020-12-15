# -*- coding: utf-8 -*-
from openerp import models, fields, api
# from openerp.exceptions import ValidationError


class BD_commandeTemplate(models.Model):
    _inherit = 'purchase.order.line'

    product_tmpl_id = fields.Many2one("product.template", string="Article", required=True, copy=True)

    # En 1er pour selectionner qu'un seul article

    @api.onchange('product_tmpl_id')
    def product_tmpl_id_change(self):
        if self.product_tmpl_id:
            product_id = self.product_tmpl_id.search([('product_tmpl_id', '=', self.product_tmpl_id.id)], limit=1)
            self.product_id = product_id.id

    @api.model
    def action_copy(self, product_id, qty):
        for i in range(int(qty)):
            new_po = product_id.copy(default="default")
        return True

    @api.multi
    def wkf_confirm_order(self, cr, uid, ids, context=None):
        for line in self.order_line:
            self.action_copy(line.product_id, line.product_qty)
        res = super(BD_commandeTemplate, self).confirm()


