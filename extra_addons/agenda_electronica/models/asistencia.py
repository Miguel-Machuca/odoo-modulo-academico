from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Asistencia(models.Model):
    _name = 'asistencia'
    _description = 'Modelo de Asistencia'
    _rec_name = 'id_afiliacion'

    id_afiliacion = fields.Many2one(
        'afiliacion',
        string='Afiliación',
        required=True,
        help='Relación entre el alumno, el curso y la gestión.'
    )
    id_cronograma = fields.Many2one(
        'cronograma',
        string='Cronograma',
        required=True,
        help='Clase específica del cronograma.'
    )
    fecha = fields.Date(
        string='Fecha',
        required=True,
        default=fields.Date.context_today
    )
    id_tipo_asistencia = fields.Many2one(
        'tipo.asistencia',
        string='Tipo de Asistencia',
        required=True,
        help='Tipo de asistencia registrada: Presente, Tarde, Ausente, etc.'
    )
    comentario = fields.Text(string='Comentario', help='Comentario adicional sobre la asistencia.')

    @api.constrains('fecha', 'id_afiliacion', 'id_cronograma')
    def _check_asistencia_unica(self):
        for record in self:
            existe = self.search_count([
                ('fecha', '=', record.fecha),
                ('id_afiliacion', '=', record.id_afiliacion.id),
                ('id_cronograma', '=', record.id_cronograma.id),
                ('id', '!=', record.id)
            ])
            if existe:
                raise ValidationError("Ya se registró asistencia para este alumno, fecha y cronograma.")

