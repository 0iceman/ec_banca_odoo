# -*- coding: utf-8 -*-

from odoo import models, fields, api

class fin_socios(models.Model):

    _inherit = 'res.partner'

    socio = fields.boolean("Socios")

