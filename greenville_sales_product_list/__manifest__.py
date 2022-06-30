# -*- coding: utf-8 -*-
{
    'name': "greenville_sales_product_list",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','website','website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_views_inherit.xml',
        'views/product_list_tag_views.xml',
        'views/partner_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
