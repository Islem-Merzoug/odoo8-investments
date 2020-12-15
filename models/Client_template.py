# -*- coding: utf-8 -*-
from openerp import models, fields, api
#from openerp.exceptions import ValidationError

class client(models.Model):
    _inherit = 'res.partner'

    @api.onchange('type_entreprise')
    def onchange_start_date(self):
        if self.type_entreprise == 'tpe':
            self.nombre_employe = 'min_10'

        if self.type_entreprise == 'pme':
            self.nombre_employe = 'min_50'

        if self.type_entreprise == 'Grand_compte':
            self.nombre_employe = 'sup_50'

    n_rc = fields.Char('N RC')
    n_ai = fields.Char('N AI')
    n_is = fields.Char('N IS')
    n_if = fields.Char('N CF')

    code_client = fields.Char('Code client')

    type_entreprise = fields.Selection([
        ('tpe', 'TPE'),
        ('pme', 'PME'),
        ('Grand_compte', 'Grand compte')])

    nombre_employe = fields.Selection([
        ('min_10', '<10'),
        ('min_50', '10-50'),
        ('sup_50', '>50')])

    etiquette = fields.Char('Etiquette')

    is_company = fields.Boolean(default='True')

    _sql_constraints = [('code_client_unique', 'unique(code_client)', 'code client exists!')]
