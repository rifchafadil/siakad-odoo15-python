from odoo import models, fields, api

class semester(models.Model):
    _name = 'rifcha.semester'
    _description = 'menyimpan data semester'

    name = fields.Char(String= 'Semester', Required = True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]

