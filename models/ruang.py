from odoo import models, fields, api

class ruang(models.Model):
    _name = 'rifcha.ruang'
    _description = 'menyimpan data ruang'

    name = fields.Char(String= 'Ruang', Required = True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]