from odoo import models, fields

class Schedule(models.Model):
    _name = 'school.schedule'
    _description = 'Schedule'
    
    teacher_id = fields.Many2one('school.teaching.load', string='Teaching Load', required=True)
    classroom_id = fields.Many2one('school.classroom', string='Classroom', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
    day_of_week = fields.Selection([
        ('0', 'Lunes'), 
        ('1', 'Martes'), 
        ('2', 'Miércoles'),
        ('3', 'Jueves'), 
        ('4', 'Viernes'), 
        ('5', 'Sábado'), 
        ('6', 'Domingo')],
        string='Day of the Week', required=True)
