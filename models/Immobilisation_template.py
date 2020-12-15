# -*- coding: utf-8 -*-
from openerp import models, fields, api
# from openerp.exceptions import ValidationError


class Immobilisation(models.Model):
    _inherit = 'account.asset.asset'

    product_tmpl_id = fields.Many2one("product.template", string="Article", required=True, copy=True)
