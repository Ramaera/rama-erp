# -*- coding: utf-8 -*-
###################################################################################
#

{
    'name': "Amount in Words in Invoice, Sale Order and Purchase Order",
    'version': '15.0.1.0.0',
    'summary': """Amount in Words in Invoice, Sale Order and Purchase Order""",
    'description': """Amount in Words in Invoice, Sale Order and Purchase Order""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'category': 'Sales',
    'depends': ['sale_management', 'account', 'purchase'],
    'data': [
        # 'views/account_move.xml',
        # 'views/sale_order_view.xml',
        # 'views/sale_order_send_mail.xml',
        # 'views/sale_order_send_without_confirm_mail.xml',
        'views/purchase_order_view.xml',
        'views/purchase_order_po_send_mail.xml',
        'views/payment_send_mail.xml',
        # 'views/invoice_send_mail.xml',
        'views/credit_note_mail_send.xml',
        'report/report.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
