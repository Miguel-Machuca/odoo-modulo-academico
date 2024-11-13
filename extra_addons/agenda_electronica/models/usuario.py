from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Modelo para ResUsers
class ResUsers(models.Model):
    _inherit = 'res.users'

    # Campo nuevo para CI
    ci = fields.Char(string="CI", required=True, help="Documento de Identificación único del usuario")

    # Campo para definir el tipo de usuario
    tipo_usuario = fields.Selection(
        [
            ('administracion', 'Administración'),
            ('apoderado', 'Apoderado'),
            ('alumno', 'Alumno'),
            ('profesor', 'Profesor')
        ],
        string="Tipo de Usuario",
        required=True
    )

    # Campos comunes
    nombre = fields.Char(string='Nombre', required=True)
    apellido_paterno = fields.Char(string='Apellido Paterno', required=True)
    apellido_materno = fields.Char(string='Apellido Materno', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')

    # Campos específicos para Administración
    puesto = fields.Selection(
        [
            ('director', 'Director'),
            ('coordinador', 'Coordinador'),
            ('secretario', 'Secretario')
        ],
        string='Puesto'
    )
    fecha_ingreso = fields.Date(string="Fecha de Ingreso")

    # Campos específicos para Apoderado
    relacion_familiar = fields.Selection(
        [
            ('padre', 'Padre'),
            ('madre', 'Madre'),
            ('tutor', 'Tutor')
        ],
        string='Relación Familiar'
    )
    direccion = fields.Text(string="Dirección")
    alumnos_ids = fields.One2many('res.users', 'apoderado_id', string="Alumnos")

    # Campos específicos para Alumno
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    grado = fields.Selection(
        [
            ('primaria', 'Primaria'),
            ('secundaria', 'Secundaria')
        ],
        string='Grado'
    )
    seccion = fields.Char(string="Sección")
    apoderado_id = fields.Many2one(
        'res.users',
        string="Apoderado",
        domain=[('tipo_usuario', '=', 'apoderado')],
        ondelete='cascade'
    )

    # Campos específicos para Profesor
    especialidad = fields.Selection(
        [
            ('matematicas', 'Matemáticas'),
            ('lenguaje', 'Lenguaje'),
            ('ciencias', 'Ciencias')
        ],
        string='Especialidad'
    )
    alumnos_profesores_ids = fields.Many2many(
        'res.users',
        'profesor_alumno_rel',  # Nombre de la tabla intermedia
        'profesor_id',         # Campo en la tabla que referencia al Profesor
        'alumno_id',           # Campo en la tabla que referencia al Alumno
        string="Alumnos"
    )

    # Validación para CI
    @api.constrains('ci')
    def _check_ci(self):
        for record in self:
            if not record.ci.isdigit():
                raise ValidationError("El CI debe contener solo números.")
            if len(record.ci) < 8 or len(record.ci) > 12:
                raise ValidationError("El CI debe tener entre 8 y 12 dígitos.")

    # Sobrescribir método create
    @api.model
    def create(self, vals):
        if 'ci' in vals:
            vals['new_password'] = vals['ci']  # Establecer CI como contraseña inicial
        user = super(ResUsers, self).create(vals)
        return user

    # Sobrescribir método write
    def write(self, vals):
        if 'ci' in vals:
            vals['new_password'] = vals['ci']  # Actualizar contraseña si cambia el CI
        return super(ResUsers, self).write(vals)
