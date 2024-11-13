from odoo import models, fields, api


class Curso(models.Model):
    _name = 'curso'
    _description = 'Modelo de Curso'
    _rec_name = 'display_name'

    nombre = fields.Char(string='Nombre', required=True)
    paralelo = fields.Char(string='Paralelo')
    display_name = fields.Char(string='Nombre Completo', compute='_compute_display_name', store=True)

    @api.depends('nombre', 'paralelo')
    def _compute_display_name(self):
        for record in self:
            if record.paralelo:
                record.display_name = f"{record.nombre} ({record.paralelo})"
            else:
                record.display_name = record.nombre or "Sin Nombre"

