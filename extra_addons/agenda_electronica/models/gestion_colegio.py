from odoo import models, fields, api

class GestionColegio(models.Model):
    _name = 'gestion.colegio'
    _description = 'Relación Gestión-Colegio'
    _rec_name = 'display_name'

    id_colegio = fields.Many2one('colegio', string='Colegio', required=True)
    id_gestion = fields.Many2one('gestion', string='Gestión', required=True)

    display_name = fields.Char(string='Nombre Completo', compute='_compute_display_name', store=True)

    _sql_constraints = [
        ('gestion_colegio_pk', 'UNIQUE(id_colegio, id_gestion)', 'La combinación de Colegio y Gestión debe ser única.')
    ]

    @api.depends('id_colegio.nombre', 'id_gestion.periodo')  # Cambiar 'name' a 'nombre' o el campo correcto
    def _compute_display_name(self):
        for record in self:
            colegio_name = record.id_colegio.nombre if record.id_colegio else "Sin Colegio"
            gestion_year = record.id_gestion.periodo if record.id_gestion else "Sin Año"
            record.display_name = f"{colegio_name} ({gestion_year})"
