# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Rama-Purchase',
    'version': '1.0',
    'category': 'Inventory/Purchase',
    'sequence': -100,
    'summary': 'Purchase orders, tenders and agreements',
    'website': 'https://www.odoo.com/app/purchase',
    'depends': ['base','purchase'],
    'data': [
        'report/purchase.report_inherit.xml'
        #
        # 'data/purchase_data.xml',
        # 'data/ir_cron_data.xml',
        # 'report/purchase_reports.xml',

    ],
    'demo': [],
    'installable': True,
    'application': False,
    # 'assets': {
    #     # 'web.assets_backend': [
    #     #     'purchase/static/src/toaster_button/*',
    #     #     'purchase/static/src/views/*.js',
    #     #     'purchase/static/src/views/*.scss',
    #     #     'purchase/static/src/js/purchase_toaster_button.js',
    #     #     'purchase/static/src/js/tours/purchase.js',
    #     #     'purchase/static/src/**/*.xml',
    #     # ],
    #     # 'web.assets_frontend': [
    #     #     'purchase/static/src/js/purchase_datetimepicker.js',
    #     #     'purchase/static/src/js/purchase_portal_sidebar.js',
    #     # ],
    # },
    'license': 'LGPL-3',
}
