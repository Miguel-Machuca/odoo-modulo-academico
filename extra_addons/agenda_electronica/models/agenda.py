from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AgendaEvento(models.Model):
    _name = 'agenda.evento'
    _description = 'Modelo de Evento para la Agenda'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre del Evento", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha_inicio = fields.Datetime(string="Fecha y Hora de Inicio", required=True)
    fecha_fin = fields.Datetime(string="Fecha y Hora de Fin", required=True)
    estado = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('confirmado', 'Confirmado'),
            ('cancelado', 'Cancelado'),
        ],
        string="Estado",
        default='pendiente',
        required=True
    )
    id_profesor = fields.Many2one(
        'res.users',
        string="Profesor",
        domain=[('tipo_usuario', '=', 'profesor')],
        help="Profesor asociado al evento"
    )
    id_alumno = fields.Many2one(
        'res.users',
        string="Alumno",
        domain=[('tipo_usuario', '=', 'alumno')],
        help="Alumno asociado al evento"
    )
    id_curso = fields.Many2one('curso', string="Curso", help="Curso asociado al evento")
    id_colegio = fields.Many2one('colegio', string="Colegio", help="Colegio asociado al evento")
    id_apoderado = fields.Many2one(
        'res.users',
        string="Apoderado",
        domain=[('tipo_usuario', '=', 'apoderado')],
        help="Apoderado asociado al evento"
    )
    participantes = fields.Many2many(
        'res.users',
        string="Participantes",
        help="Otros participantes del evento (alumnos, profesores, apoderados)"
    )

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_inicio >= record.fecha_fin:
                raise ValidationError("La fecha de inicio debe ser menor que la fecha de fin.")
