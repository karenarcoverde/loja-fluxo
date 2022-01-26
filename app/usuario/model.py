from ..extensions import db

# Usuario
# tabela que contem as configurações do usuário
# id => chave primária
# nome => nome completo do usuário
# cpf => CPF do usuário
# email => email do usuário
# telefone => telefone residencial ou celular do usuário
# endereço => endereço completo do usuário: rua, número, complemento etc.

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    cpf = db.Column(db.Integer, unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    telefone = db.Column(db.Integer, nullable = False)
    endereco = db.Column(db.String(30), nullable = False)

    # carrinho(one) <-> usuario(one)
    carrinho = db.relationship("carrinho", back_populates="usuario", uselist=False)

    # cupons(many) <-> usuario(one)
    cupom = db.relationship('Cupons', backref = 'cupons_usuario')

    def json(self):
            return{
                'nome':self.nome,
                'cpf':self.cpf,
                'email':self.email,
                'telefone':self.telefone,
                'endereco':self.endereco,
                'carrinho_id':self.carrinho_id
            }