from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.carrinho.model import Carrinho

class CarrinhoDetalhes(MethodView): 
    def get(self):
        carrinhos = Carrinho.query.all()
        return jsonify([carrinho.json() for carrinho in carrinhos]),200

    def post(self):
        dados = request.json        
        forma_pagamento = dados.get('forma_pagamento')
        preco_frete = dados.get('preco_frete')
        quantidade = dados.get('quantidade')
        preco_total = dados.get('preco_total')


        if isinstance (forma_pagamento,str) and isinstance (preco_frete,int) and isinstance (quantidade,int) and isinstance (preco_total,int):
            carrinho = Carrinho(forma_pagamento= forma_pagamento, preco_frete = preco_frete, quantidade = quantidade, preco_total = preco_total)
            db.session.add(carrinho)
            db.session.commit()
            return carrinho.json(),200
        return {"code_status":"invalid data in request"},400