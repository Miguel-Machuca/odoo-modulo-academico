from odoo import models, fields


class Vinculacion(models.Model):
    _name = 'vinculacion'
    _description = 'Relación entre Alumno y Apoderado'

    id_apoderado = fields.Many2one(
        'res.users', 
        string='Apoderado', 
        required=True, 
        domain=[('tipo_usuario', '=', 'apoderado')]
    )
    id_afiliacion = fields.Many2one(
        'afiliacion', 
        string='Afiliación', 
        required=True, 
        help='Afiliación relacionada con el alumno'
    )
    afinidad = fields.Char(string='Afinidad')

    # Sin restricciones únicas
