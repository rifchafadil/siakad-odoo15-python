from odoo import api, fields, models


class dosen(models.Model):
    _name = 'rifcha.dosen'
    _description = 'menyimpan data dosen'

    name = fields.Char(String= 'Nama Dosen', Required = True)
    nip = fields.Char(String= 'NIP', Required = True)
    image = fields.Binary(string='Image', attachment=True, required=True)
    matakuliah = fields.Many2many(string="Mata kuliah",comodel_name="rifcha.matakuliah",ondelete="restrict")
    fakultas = fields.Many2one(string="Fakultas",comodel_name="rifcha.fakultas",ondelete="restrict")
    prodi = fields.Many2one(string="Program Studi",comodel_name="rifcha.prodi",ondelete="restrict")

    sd = fields.Char(String= 'SD', Required = True)
    smp = fields.Char(String= 'SMP', Required = True)
    sma = fields.Char(String= 'SMA', Required = True)
    pt = fields.Char(String= 'Perguruan Tinggi', Required = True)

    email = fields.Char(String= 'Email', Required = True)
    telp = fields.Char(String= 'Nomor Telepon', Required = True)
    alamat = fields.Char(String= 'Alamat', Required = True)

    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]

