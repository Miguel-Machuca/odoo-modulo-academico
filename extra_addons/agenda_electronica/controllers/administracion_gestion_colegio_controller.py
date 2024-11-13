from odoo import http
from odoo.http import request


class AdminGestionColegioController(http.Controller):
    @http.route('/administracion/log_access', type='http', auth='user', website=False)
    def log_access(self):
        user = request.env.user
        admin_gestion = request.env['administracion.gestion.colegio'].create({
            'id_administracion': user.id if user.tipo_usuario == 'administracion' else None,
            'id_colegio': None,  # Rellenar con lógica si aplica
            'id_gestion': None,  # Rellenar con lógica si aplica
        })
        return "Acceso registrado"
