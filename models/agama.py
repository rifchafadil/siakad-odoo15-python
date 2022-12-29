from odoo import models, fields, api

class agama(models.Model):
    _name = 'rifcha.agama'
    _description = 'menyimpan data agama'

    name = fields.Char(String= 'Agama', Required = True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]

