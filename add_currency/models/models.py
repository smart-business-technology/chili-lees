# -*- coding: utf-8 -*-

from odoo import models, fields, api


class add_currency(models.Model):
    _name = 'hr.contract'

    curr = fields.Selection(string="", selection=[('dollar', 'الدولار'), ('dinar', 'الدينار العراقي'), ], required=False, )