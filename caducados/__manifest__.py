# -*- coding: utf-8 -*-
{
    'name': "caducados",

    'summary': """Muestra solo los lotes que no están caducados""",

    'description': """
        Muestra solo los lotes que no están caducados
    """,

    'author': "PABLO CASTELO",
    'website': "http://www.zverp.com",
    'license': "GPL-2",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'product_expiry'],

    # always loaded
    'data': [
    ],
}
