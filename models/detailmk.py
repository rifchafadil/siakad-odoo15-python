from odoo import models, fields, api

class detailmk(models.Model):
    _name = 'rifcha.detailmk'
    _description = 'menyimpan data detailmk'

    nim = fields.Many2one(string="Nama Mahasiswa",comodel_name="rifcha.mahasiswa",ondelete="restrict")
    kodeMK = fields.Many2one(string="Nama Matakuliah",comodel_name="rifcha.matakuliah",ondelete="restrict")
    name = fields.Many2one(string="Semester",comodel_name="rifcha.semester",ondelete="restrict")
    uts = fields.Float(string= 'Nilai UTS', required = True)
    uas = fields.Float(string= 'Nilai UAS', required = True)
    tugas = fields.Float(string= 'Nilai Tugas', required = True)
    quiz = fields.Float(string= 'Nilai Quiz', required = True)
    
    total = fields.Float(compute="_compute_total")

    @api.depends("uts", "uas", "tugas", "quiz")
    def _compute_total(self):
        for record in self:
            record.total = (0.15 * record.uts) + (0.15 * record.uas) + (0.50 * record.tugas) + (0.20 * record.quiz)