from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.produtos.model import Produtos

class ProdutosDetalhes(MethodView): 
    def get(self):
        produtos = Produtos.query.all()
        return jsonify([produto.json() for produto in produtos]),200

    def post(self):
        dados = request.json        
        nome_produto = dados.get('nome_produto')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        validade = dados.get('validade')

        if isinstance (nome_produto,str) and isinstance (descricao,str) and isinstance (preco,int) and isinstance (validade,int):
            produto = Produtos(nome_produto= nome_produto, descricao = descricao, preco = preco, validade = validade)
            db.session.add(produto)
            db.session.commit()
            return produto.json(),200
        return {"code_status":"invalid data in request"},400