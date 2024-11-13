from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Cronograma(models.Model):
    _name = 'cronograma'
    _description = 'Modelo de Cronograma'
    _rec_name = 'display_name'

    id_materia = fields.Many2one('materia', string='Materia', required=True)
    id_curso = fields.Many2one('curso', string='Curso', required=True)
    id_profesor = fields.Many2one(
        'res.users', 
        string='Profesor', 
        required=True, 
        domain=[('tipo_usuario', '=', 'profesor')]
    )

    # Campos de hora
    hora_inicio = fields.Float(
        string='Hora de Inicio',
        required=True,
        help="Ingrese la hora en formato decimal (por ejemplo, 13.5 para 13:30)."
    )
    hora_fin = fields.Float(
        string='Hora de Fin',
        required=True,
        help="Ingrese la hora en formato decimal (por ejemplo, 15.75 para 15:45)."
    )

    # Campos computados para mostrar las horas en formato hh:mm
    hora_inicio_display = fields.Char(
        string='Hora de Inicio (Formato hh:mm)',
        compute='_compute_hora_inicio_display',
        store=False
    )
    hora_fin_display = fields.Char(
        string='Hora de Fin (Formato hh:mm)',
        compute='_compute_hora_fin_display',
        store=False
    )

    @api.depends('hora_inicio')
    def _compute_hora_inicio_display(self):
        for record in self:
            if record.hora_inicio:
                horas = int(record.hora_inicio)
                minutos = int((record.hora_inicio - horas) * 60)
                record.hora_inicio_display = f"{horas:02}:{minutos:02}"
            else:
                record.hora_inicio_display = "Sin Hora"

    @api.depends('hora_fin')
    def _compute_hora_fin_display(self):
        for record in self:
            if record.hora_fin:
                horas = int(record.hora_fin)
                minutos = int((record.hora_fin - horas) * 60)
                record.hora_fin_display = f"{horas:02}:{minutos:02}"
            else:
                record.hora_fin_display = "Sin Hora"

    dias = fields.Selection(
        string='Días de la Semana',
        selection=[
            ('lunes', 'Lunes'),
            ('martes', 'Martes'),
            ('miercoles', 'Miércoles'),
            ('jueves', 'Jueves'),
            ('viernes', 'Viernes'),
            ('sabado', 'Sábado'),
            ('domingo', 'Domingo'),
        ],
        required=True,
        help="Selecciona el día de la semana para este cronograma."
    )

    display_name = fields.Char(
        string='Nombre Completo',
        compute='_compute_display_name',
        store=True
    )
    
    @api.depends('id_materia', 'id_curso')
    def _compute_display_name(self):
        for record in self:
            materia_name = record.id_materia.nombre if record.id_materia else "Sin Materia"
            curso_name = record.id_curso.display_name if record.id_curso else "Sin Curso"
            record.display_name = f"{materia_name} - {curso_name}"

    @api.constrains('hora_inicio', 'hora_fin')
    def _check_horas(self):
        for record in self:
            if record.hora_inicio >= record.hora_fin:
                raise ValidationError("La hora de inicio debe ser menor que la hora de fin.")
