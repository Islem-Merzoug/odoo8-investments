# -*- coding: utf-8 -*-
from openerp import models, fields, api
# from openerp.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    state = fields.Selection([
        ('brouillon', "Brouillon"),
        ('pret', "Prêt"),
        ('transferé', "Transféré"),
    ], default='brouillon')

    @api.multi
    def pret_action(self):
        return self.write({'state': 'pret'})

    @api.multi
    def transfere_action(self):
        return self.write({'state': 'transferé'})


    def get_default_investissment_type(self):
        return 'is_investissement' in self.env.context

        # if self._context.get('is_invesstissement'):  # Dans le domaine de l'action la clé est: `is_investissement`
        #     return True
        #
        # else:
        #     return False

    is_investissement = fields.Boolean(default=get_default_investissment_type)

