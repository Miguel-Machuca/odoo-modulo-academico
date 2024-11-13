from odoo import models, fields


class Gestion(models.Model):
    _name = 'gestion'
    _description = 'Modelo de Gestión'
    _rec_name = 'periodo'

    periodo = fields.Char(string='Año', required=True)