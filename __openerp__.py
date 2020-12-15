# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Investissements',
    'version': '1.0',
    'category': 'champ ',
    'description': """ 17 ! """,
    'author': 'Salamo !',
    'depends': [
        'base',
        'product',
        'purchase',
        'account',
    ],
    'data': [
        'views/Client_views.xml',
        'views/Article_views.xml',
        'views/menus.xml',
        'views/BD_Commande_views .xml',
        'views/Immobilisation_views.xml'
        # 'views/Service_views.xml',
        # 'views/Workflow_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
