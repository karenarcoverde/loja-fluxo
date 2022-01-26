from flask import Blueprint

from app.produtos.controller import ProdutosDetalhes, ProdutosId

produtos_api = Blueprint('produtos_api', __name__)

produtos_api.add_url_rule(
    '/produtos', view_func= ProdutosDetalhes.as_view('Produtos_detalhes'), methods=['GET','POST']
)

produtos_api.add_url_rule(
    '/produtos/<int:id>', view_func= ProdutosId.as_view('produtos_id'), methods=['GET','PUT', 'PATCH','DELETE']
)