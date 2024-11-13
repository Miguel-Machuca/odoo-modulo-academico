{
    'name': 'Agenda Electronica Academica',
    'version': '1.0',
    'summary': 'Módulo de Agenda Academica Electronica para Colegio',
    'description': """
        This module allows you to manage the entire infrastructure of a school including:
        - Alumno
        - Profesor
        - Gestion
        - Cronograma
        - Materia
        - Agenda
        - Comunicado
    """,
    'author': 'sw1-grupo7',
    'website': 'http://www.website.com',
    'category': 'Educación',
    'depends': ['base', 'hr','hr_attendance'],
    'data': [
        'security/groups.xml',
        
        'security/ir.model.access.csv',
        'data/email_template_user_password.xml',
        'views/menu.xml',
        'views/colegio_views.xml',                   
        'views/alumno_views.xml',  
        'views/apoderado_views.xml',  
        'views/administracion_views.xml',  
        'views/profesor_views.xml',
        'views/gestion_views.xml',
        'views/curso_views.xml',
        'views/afiliacion_views.xml',
        'views/materia_views.xml',  
        'views/vinculacion_views.xml',  
        'views/cronograma_views.xml',
        'views/tipo_asistencia_views.xml',
        'views/asistencia_views.xml',
        'views/agenda_views.xml',
        'views/comunicados_views.xml',
        

    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
