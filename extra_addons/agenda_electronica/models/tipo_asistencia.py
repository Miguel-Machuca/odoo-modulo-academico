from odoo import models, fields

class TipoAsistencia(models.Model):
    _name = 'tipo.asistencia'
    _description = 'Modelo de Tipo de Asistencia'

    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)