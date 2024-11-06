# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BaseNameDisplay(models.AbstractModel):
    _name = 'base.name.display'
    _description = 'Base Model for Displaying Name'

    name = fields.Char(compute='_compute_name', store=True)

    @api.depends('nombre')
    def _compute_name(self):
        for record in self:
            record.name = record.nombre


class gestion_academica(models.Model):
     _name = 'gestion_academica.gestion_academica'
     _inherit = 'base.name.display'
     _description = 'gestion_academica.gestion_academica'

     nombre = fields.Char()
     gestion = fields.Char()
     nombre_director = fields.Char()
     departamento = fields.Char()
     provincia = fields.Char()
     direccion = fields.Char()
     telefono = fields.Char()
     
     profesores_ids = fields.One2many('gestion_academica.profesor', 'gestion_academica_id', string='Profesores')
     aulas_ids = fields.One2many('gestion_academica.aula', 'gestion_academica_id', string='Aulas')

class aula(models.Model):
     _name = 'gestion_academica.aula'
     _inherit = 'base.name.display'
     _description = 'gestion_academica.aula'

     nombre = fields.Char()
     seccion = fields.Char()
     horario = fields.Char()
     
     alumnos_ids = fields.One2many('gestion_academica.alumno', 'aula_id', string='Alumnos')
     gestion_academica_id = fields.Many2one('gestion_academica.gestion_academica', string='Colegio')

class profesor(models.Model):
     _name = 'gestion_academica.profesor'
     _inherit = 'base.name.display'
     _description = 'gestion_academica.profesor'

     nombre = fields.Char()
     apellido = fields.Char()     
     fecha_nacimiento = fields.Char()
     direccion = fields.Char()     
     ci = fields.Char()

     gestion_academica_id = fields.Many2one('gestion_academica.gestion_academica', string='Colegio')
     materias_ids = fields.Many2many('gestion_academica.materia', string='Materias impartidas')

class materia(models.Model):
     _name = 'gestion_academica.materia'
     _inherit = 'base.name.display'
     _description = 'gestion_academica.materia'

     nombre = fields.Char()
     codigo = fields.Char()  

     calificaciones_ids = fields.One2many('gestion_academica.calificacion', 'materia_id', string='Calificaciones')
     profesores_ids = fields.Many2many('gestion_academica.profesor', string='Profesores')

class alumno(models.Model):
     _name = 'gestion_academica.alumno'
     _inherit = 'base.name.display'
     _description = 'gestion_academica.alumno'

     nombre = fields.Char()
     apellido_paterno = fields.Char()
     apellido_materno = fields.Char()
     fecha_nacimiento = fields.Char()
     direccion = fields.Char()
     ci = fields.Char()

     calificaciones_ids = fields.One2many('gestion_academica.calificacion', 'alumno_id', string='Calificaciones')
     aula_id = fields.Many2one('gestion_academica.aula', string='Aula')

class calificacion(models.Model):
     _name = 'gestion_academica.calificacion'
     _description = 'gestion_academica.calificacion'

     nota = fields.Char()
     
     alumno_id = fields.Many2one('gestion_academica.alumno', string='Alumno')
     materia_id = fields.Many2one('gestion_academica.materia', string='Materia')
     