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

        if Usuario.query.filter_by(cpf = cpf).first():
            return{"error":"CPF já cadastrado"}
        if Usuario.query.filter_by(email = email).first():
            return{"error":"E-mail já cadastrado"}

        if isinstance (nome,str) and isinstance (cpf,str) and isinstance (email,str):
            usuario = Usuario(nome = nome, cpf = cpf, email = email, telefone = telefone, endereco = endereco)
            db.session.add(usuario)
            db.session.commit()
            return usuario.json(),200
        return {"code_status":"invalid data in request"},400

class UsuarioId(MethodView):
    def get (self,id):
        usuario = Usuario.query.get_or_404(id)
        return usuario.json()

    def put (self,id):
        dados = request.json
        nome = dados.get('nome')
        cpf = dados.get('cpf')
        email = dados.get('email')
        telefone = dados.get('telefone')
        endereco = dados.get('endereco')

        if isinstance (nome,str) and isinstance (cpf,str) and isinstance (email,str):
            usuario = Usuario.query.get_or_404(id)
            usuario.nome = nome
            usuario.cpf = cpf
            usuario.email = email
            usuario.telefone = telefone
            usuario.endereco = endereco
            db.session.commit()
            return usuario.json(),200
        return {"code_status":"invalid data in request"},400

    def patch (self,id):
        dados = request.json
        usuario = Usuario.query.get_or_404 (id)
  
        nome = dados.get('nome',Usuario.nome)
        cpf = dados.get('cpf', Usuario.cpf)
        email = dados.get('email',Usuario.email)
        telefone = dados.get('telefone',Usuario.telefone)
        endereco = dados.get('endereco',Usuario.endereco)

        if isinstance (nome,str) and isinstance (cpf,str) and isinstance (telefone,str) and isinstance (endereco,str):
            usuario.nome = nome
            usuario.cpf = cpf
            usuario.email = email
            usuario.telefone = telefone
            usuario.endereco = endereco
            db.session.commit()
            return usuario.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        usuario = Usuario.query.get_or_404(id)
        db.session.delete (usuario)
        db.session.commit ()
        return {"code_status":"deletado"},200

