from odoo import models, fields, api

class fakultas(models.Model):
    _name = 'rifcha.fakultas'
    _description = 'menyimpan data fakultas'

    name = fields.Char(string= 'Nama Fakultas', required = True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]