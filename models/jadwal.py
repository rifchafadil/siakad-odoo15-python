from odoo import models, fields, api

class jadwal(models.Model):
    _name = 'rifcha.jadwal'
    _description = 'menyimpan data jadwal'

    kodeJadwal = fields.Char(string= 'Kode Jadwal', required = True)
    name = fields.Many2one(string="Nama Mata kuliah",comodel_name="rifcha.matakuliah",ondelete="restrict")
    hari = fields.Many2one(string="Hari",comodel_name="rifcha.hari",ondelete="restrict")
    prodi_id = fields.Many2one(string="Nama Prodi",comodel_name="rifcha.prodi",ondelete="restrict")
    jam_mulai = fields.Float(string= 'Jam Mulai', required = True)
    jam_selesai = fields.Float(string= 'Jam Selesai', required = True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]
    
