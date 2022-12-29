from odoo import models, fields, api

class prodi(models.Model):
    _name = 'rifcha.prodi'
    _description = 'menyimpan data prodi'

    name = fields.Char(string= 'Nama Prodi', required = True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]
    fakultas_id = fields.Many2one(string="Nama Fakultas",comodel_name="rifcha.fakultas",ondelete="restrict")