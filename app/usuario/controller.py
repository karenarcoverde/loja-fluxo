from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.usuario.model import Usuario

class UsuarioDetalhes(MethodView): 
    def get(self):
        usuarios = Usuario.query.all()
        return jsonify([usuario.json() for usuario in usuarios]),200

    def post(self):
        dados = request.json        
        nome = dados.get('nome')
        cpf = dados.get('cpf')
        email = dados.get('email')
        telefone = dados.get('telefone')
        endereco = dados.get('endereco')
        carrinho_id = dados.get('carrinho_id')

        if Usuario.query.filter_by(cpf = cpf ).first():
            return{"error":"CPF já cadastrado"}
        if Usuario.query.filter_by(email = email ).first():
            return{"error":"E-mail já cadastrado"}

        if isinstance (nome,str) and isinstance (cpf,int) and isinstance (email,str):
            usuario = Usuario(nome = nome, cpf = cpf, email = email, telefone = telefone, endereco = endereco, carrinho_id = carrinho_id)
            usuario.save()
            db.session.add(usuario)
            db.session.commit()
            return usuario.json(),200
        return {"code_status":"invalid data in request"},400