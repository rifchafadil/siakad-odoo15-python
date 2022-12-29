from odoo import models, fields, api

class matakuliah(models.Model):
    _name = 'rifcha.matakuliah'
    _description = 'menyimpan data matakuliah'

    kodeMK = fields.Char(string= 'Kode Matakuliah', required = True)
    name = fields.Char(string= 'Nama Matakuliah', required = True)
    SKS = fields.Char(string= 'Sistem Kredit Semester', required = True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]