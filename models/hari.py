from odoo import models, fields, api

class hari(models.Model):
    _name = 'rifcha.hari'
    _description = 'menyimpan data hari'

    name = fields.Char(String= 'Nama hari', Required = True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]
