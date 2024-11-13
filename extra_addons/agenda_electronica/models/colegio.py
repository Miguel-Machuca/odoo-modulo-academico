from odoo import models, fields

class Colegio(models.Model):
    _name = 'colegio'
    _description = 'Modelo de Colegio'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')