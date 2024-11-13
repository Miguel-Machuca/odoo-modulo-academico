from odoo import models, fields

class Materia(models.Model):
    _name = 'materia'
    _description = 'Modelo de Materia'
    _rec_name = 'nombre'


    nombre = fields.Char(string='Nombre', required=True)
