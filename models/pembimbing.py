from odoo import models, fields, api

class pembimbing(models.Model):
    _name = 'rifcha.pembimbing'
    _description = 'menyimpan data pembimbing'

    name = fields.Char(String= 'Dosen Pembimbing', Required = True)
    nip = fields.Char(String= 'NIP', Required = True) 
    email = fields.Char(String= 'Email', Required = True)
    prodi_id = fields.Many2one(string="Nama Prodi",comodel_name="rifcha.prodi",ondelete="restrict")
    image = fields.Binary(string='Image', attachment=True, required=True)
    _sql_constraints = [('name_uniq', 'unique(name)', 'data sudah ada')]

