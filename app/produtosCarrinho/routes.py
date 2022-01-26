from flask import Blueprint

from app.produtosCarrinho.controller import ProdutosCarrinhoDetalhes, ProdutosCarrinhoId

produtoscarrinho_api = Blueprint('produtoscarrinho_api', __name__)

produtoscarrinho_api.add_url_rule(
    '/produtoscarrinho', view_func= ProdutosCarrinhoDetalhes.as_view('produtoscarrinho_detalhes'), methods=['GET','POST']
)

produtoscarrinho_api.add_url_rule(
    '/produtoscarrinho/<int:id>', view_func= ProdutosCarrinhoId.as_view('produtoscarrinho_id'), methods=['GET','PUT', 'PATCH','DELETE']
)