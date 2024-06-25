# -*- coding: utf-8 -*-

# Created on 20120-01-05
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo12在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/12.0/zh_CN/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/

##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "NFC reader writer, nfc rfid support with product nfc",
    'version': '13.21.12.21',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 68.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'depends': [
        'web',
        'product',
        'app_common',
    ],
    'summary': '''
    NFC Read and Write widget.
    Easy use in any app and char field.
    Various NFC standard support. Like ISO 14443,15693.
    Demo view for product nfc read and write in barcode field.
    ''',
    'description': '''    
    Support Odoo 13，12, Enterprise and Community Edition
    1. NFC Read and Write widget in odoo
    2. Easy use in any app and char field。 options={'nfcw':1, 'nfcr':1, 'nfcr_auto':1, 'nfcr_data':0 }
    3. Support Chrome only V89+, Android 10+
    4. Various NFC standard support. Like NFC-A (ISO 14443-3A)/NFC-B (ISO 14443-3B)/NFC-F (JIS 6319-4)/NFC-V (ISO 15693)/ISO-DEP (ISO 14443-4)  
    5. Demo view for product nfc read and write in barcode field
    6. Note: Only 1 field can be rfid reader in one form view.
    11. Multi-language Support.
    12. Multi-Company Support.
    13. Support Odoo 13，12, Enterprise and Community Edition
    ==========
    1. 
    2. 
    11. 多语言支持
    12. 多公司支持
    13. Odoo 13, 12, 企业版，社区版，多版本支持
    ''',
    'data': [
        # 'security/*.xml',
        # 'security/ir.model.access.csv',
        # 'data/.xml',
        'views/webclient_templates.xml',
        'views/product_product_views.xml',
        # 'report/.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
