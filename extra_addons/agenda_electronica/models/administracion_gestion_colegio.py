from odoo import models, fields


class AdministracionGestionColegio(models.Model):
    _name = 'administracion.gestion.colegio'
    _description = 'Relación Administración-Gestión-Colegio'

    id_administracion = fields.Many2one('administracion', string='Administración', required=True)
    id_colegio = fields.Many2one('colegio', string='Colegio', required=True)
    id_gestion = fields.Many2one('gestion', string='Gestión', required=True)
    fecha_hora_creacion = fields.Datetime(string='Fecha y Hora de Creación', default=fields.Datetime.now, required=True)

    _sql_constraints = [
        ('administracion_gestion_colegio_pk', 'UNIQUE(id_administracion, id_colegio, id_gestion)', 'La combinación debe ser única.')
    ]
