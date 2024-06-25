# -*- coding: utf-8 -*-

from odoo import fields, models, api, tools, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)

class mytest(models.Model):
    _name = 'mytest.mytest'
    _inherit = 'res.partner'
    _order = 'sequence'

    name = fields.Char(string='Name')
    ref = fields.Char(string='Internal Reference', default=_('New'), index=True, copy=False)
    value = fields.Integer(string='value')
    value2 = fields.Float(string='value2', compute="_compute_value", inverse='_set_value', store=True, readonly=1)
    date = fields.Date('Order Date', required=True, readonly=True, states={'draft': [('readonly', False)]},
                       default=fields.Date.context_today)
    date_begin = fields.Datetime(string='Date Begin', index=True, default=fields.Datetime.now)
    product_id = fields.Many2one('product.product', index=True, ondelete='cascade', readonly=True)
    move_dest_ids = fields.One2many('stock.move', 'created_production_id', string="Stock Movements of Produced Goods")

    user_ids = fields.Many2many('res.users', string='Salesmen')
    note = fields.Text()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], required=True, default='draft', string='State')
    sequence = fields.Integer('Sequence', default=20, help="Determine the display order. Sort ascending.")
    active = fields.Boolean('Active', default=True)


    @api.depends('value')
    def _compute_value(self):
        self.value2 = float(self.value) / 100

    def _set_value(self):
        pass
