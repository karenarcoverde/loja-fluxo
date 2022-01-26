from flask import Blueprint

from app.usuario.controller import UsuarioDetalhes

usuario_api = Blueprint('usuario_api', __name__)

usuario_api.add_url_rule(
    '/usuarios', view_func= UsuarioDetalhes.as_view('usuario_detalhes'), methods=['GET','POST']
)
