from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.novidades.model import Novidades

class NovidadesDetalhes(MethodView): 
    def get(self):
        novidades = Novidades.query.all()
        return jsonify([novidade.json() for novidade in novidades]),200

    def post(self):
        dados = request.json        
        nome_novidade = dados.get('nome_novidade')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        validade = dados.get('validade')
        data_lancamento = dados.get('data_lancamento')


        if isinstance (nome_novidade,str) and isinstance (descricao,str) and isinstance (preco,int) and isinstance (validade,str) and isinstance (data_lancamento,str):
            novidade = Novidades(nome_novidade= nome_novidade, descricao = descricao, preco = preco, validade = validade, data_lancamento = data_lancamento )
            db.session.add(novidade)
            db.session.commit()
            return novidade.json(),200
        return {"code_status":"invalid data in request"},400

class NovidadesId(MethodView):
    def get (self,id):
        novidade = Novidades.query.get_or_404(id)
        return novidade.json()

    def put (self,id):
        dados = request.json
        nome_novidade = dados.get('nome_novidade')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        validade = dados.get('validade')
        data_lancamento = dados.get('data_lancamento')


        novidade = Novidades.query.get_or_404(id)
        novidade.nome_novidade = nome_novidade
        novidade.descricao = descricao
        novidade.preco = preco
        novidade.validade = validade
        novidade.data_lancamento = data_lancamento
        db.session.commit()
        return novidade.json(),200
      

    def patch (self,id):
        dados = request.json
        novidade= Novidades.query.get_or_404 (id)
  
        nome_novidade= dados.get('nome_novidade',Novidades.nome_novidade)
        descricao = dados.get('descricao', Novidades.descricao)
        preco = dados.get('preco',Novidades.preco)
        validade = dados.get('validade',Novidades.validade)
        data_lancamento = dados.get('data_lancamento',Novidades.data_lancamento)

        novidade.nome_novidade = nome_novidade
        novidade.descricao = descricao
        novidade.preco = preco
        novidade.validade = validade
        novidade.data_lancamento = data_lancamento
        db.session.commit()
        return novidade.json(),200
    

    def delete(self,id):
        novidade = Novidades.query.get_or_404(id)
        db.session.delete (novidade)
        db.session.commit ()
        return {"code_status":"deletado"},200

