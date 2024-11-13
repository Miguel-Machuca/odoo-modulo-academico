from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Comunicado(models.Model):
    _name = 'comunicado'
    _description = 'Modelo de Comunicados'
    _rec_name = 'titulo'

    titulo = fields.Char(string="Título", required=True)
    descripcion = fields.Text(string="Descripción", required=True)
    fecha_publicacion = fields.Datetime(string="Fecha de Publicación", required=True)
    estado = fields.Selection(
        [
            ('borrador', 'Borrador'),
            ('publicado', 'Publicado'),
            ('cancelado', 'Cancelado'),
        ],
        string="Estado",
        default='borrador',
        required=True
    )
    id_curso = fields.Many2one('curso', string="Curso", help="Curso asociado al comunicado.")
    
    destinatarios_profesores = fields.Many2many(
        'res.users',
        'comunicado_profesor_rel',  # Nombre único de la tabla intermedia
        'comunicado_id',            # Nombre de la columna que referencia al modelo actual
        'profesor_id',              # Nombre de la columna que referencia al modelo 'res.users'
        string="Profesores",
        domain=[('tipo_usuario', '=', 'profesor')],
        help="Profesores destinatarios del comunicado."
    )
    destinatarios_alumnos = fields.Many2many(
        'res.users',
        'comunicado_alumno_rel',    # Nombre único de la tabla intermedia
        'comunicado_id',            # Nombre de la columna que referencia al modelo actual
        'alumno_id',                # Nombre de la columna que referencia al modelo 'res.users'
        string="Alumnos",
        domain=[('tipo_usuario', '=', 'alumno')],
        help="Alumnos destinatarios del comunicado."
    )
    destinatarios_apoderados = fields.Many2many(
        'res.users',
        'comunicado_apoderado_rel', # Nombre único de la tabla intermedia
        'comunicado_id',            # Nombre de la columna que referencia al modelo actual
        'apoderado_id',             # Nombre de la columna que referencia al modelo 'res.users'
        string="Apoderados",
        domain=[('tipo_usuario', '=', 'apoderado')],
        help="Apoderados destinatarios del comunicado."
    )
    destinatarios_administracion = fields.Many2many(
        'res.users',
        'comunicado_administracion_rel', # Nombre único de la tabla intermedia
        'comunicado_id',                 # Nombre de la columna que referencia al modelo actual
        'administracion_id',             # Nombre de la columna que referencia al modelo 'res.users'
        string="Administración",
        domain=[('tipo_usuario', '=', 'administracion')],
        help="Administración destinataria del comunicado."
    )

    @api.constrains('fecha_publicacion')
    def _check_fecha_publicacion(self):
        for record in self:
            if record.fecha_publicacion < fields.Datetime.now():
                raise ValidationError("La fecha de publicación no puede ser en el pasado.")
