from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.users"

    prodi_ids = fields.Many2many("rifcha.prodi", string="Program Studi")