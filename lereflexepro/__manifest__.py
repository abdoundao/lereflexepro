# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'lereflexepro',
    'version': '15.0.0.0',
    'category': "Project",
    'license': 'OPL-1',
    'summary': 'Le reflexe pro',
    'description': """Project Template , Make project as template and make new project from the Template, """,
    'author': 'Abdou NDAO',
    'website': 'https://www.lereflexeprohygiene.coom',
    'depends': ['base', 'sale', 'purchase', 'account', 'vista_backend_theme'],
    'data': [
        'security/ir.model.access.csv',
        'report/rapport_intervention.xml',
        'views/move.xml',

    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    "images": ['static/description/Banner.png'],
}
