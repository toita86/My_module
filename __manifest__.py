# -*- coding: utf-8 -*-

{
    'name': 'My module',
    'version': '1.0',
    '0': 'Sales/My module',
    'summary': 'The best odoo exstension in the world' ,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        
        'views/data_property_views.xml',
        'views/data_menus.xml',

        'views/type_property_views.xml',

        'views/tag_property_views.xml',

        'views/offers_property_views.xml',

        'views/inherited_property_views.xml'
    ]
}
