from odoo import models, fields, api

class Mahasiswa(models.Model):
    _name = 'rifcha.mahasiswa'
    _description = 'menyimpan data mahasiswa'

    name = fields.Char(string= 'Nama Mahasiswa', required = True)
    nim = fields.Char(string= 'NIM Mahasiswa', required = True)
    alamat = fields.Char(string= 'Alamat Mahasiswa', required = True)
    telp = fields.Char(string= 'Telepon Mahasiswa', required = True)
    agama_id = fields.Many2one(string="Nama Agama",comodel_name="rifcha.agama",ondelete="restrict")
    image = fields.Binary(string='Image', attachment=True, required=True)

    ayah = fields.Char(string= 'Nama Ayah', required = True)
    ibu = fields.Char(string= 'Nama Ibu', required = True)
    pekerjaanayah = fields.Char(string= 'Pekerjaan Ayah', required = True)
    pekerjaanibu = fields.Char(string= 'Pekerjaan Ibu', required = True)

    _sql_constraints = [('nim_uniq', 'unique(name)', 'data sudah ada')]
