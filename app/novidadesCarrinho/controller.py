from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.novidadesCarrinho.model import NovidadesCarrinho

class NovidadesCarrinhoDetalhes(MethodView): 
    def get(self):
        novidadescarrinho = NovidadesCarrinho.query.all()
        return jsonify([novidadecarrinho.json() for novidadecarrinho in novidadescarrinho]),200

    def post(self):
        dados = request.json        
        nome_novidade = dados.get('nome_novidade')
        quantidade = dados.get('quantidade')
        preco_total = dados.get('preco_total')
       
        if isinstance (nome_novidade,str) and isinstance (quantidade,int) and isinstance (preco_total,int):
            novidadecarrinho = NovidadesCarrinho(nome_novidade= nome_novidade, quantidade = quantidade, preco_total = preco_total)
            db.session.add(novidadecarrinho)
            db.session.commit()
            return novidadecarrinho .json(),200
        return {"code_status":"invalid data in request"},400