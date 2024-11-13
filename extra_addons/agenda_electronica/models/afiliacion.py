from odoo import models, fields, api

class Afiliacion(models.Model):
    _name = 'afiliacion'
    _description = 'Modelo de Afiliación'
    _rec_name = 'display_name'

    id_alumno = fields.Many2one(
        'res.users',
        string='Alumno',
        required=True,
        ondelete='cascade',
        domain=[('tipo_usuario', '=', 'alumno')]
    )
    id_gestion_colegio = fields.Many2one(
        'gestion.colegio',
        string='Gestión-Colegio',
        required=True,
        ondelete='cascade',
        help='Relación entre la Gestión y el Colegio'
    )
    id_curso = fields.Many2one(
        'curso',
        string='Curso',
        required=True,
        ondelete='cascade',
        help='Curso asignado al alumno'
    )
    fecha = fields.Date(string='Fecha', required=True)

    display_name = fields.Char(string='Nombre del Alumno', compute='_compute_display_name', store=True)

    _sql_constraints = [
        ('afiliacion_pk', 'UNIQUE(id_alumno, id_gestion_colegio, id_curso, fecha)', 
         'Un alumno no puede tener múltiples afiliaciones al mismo curso en la misma gestión y fecha.')
    ]

    @api.depends('id_alumno.name')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.id_alumno.name if record.id_alumno else "Sin Alumno"
