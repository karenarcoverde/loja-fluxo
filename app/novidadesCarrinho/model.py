from app.extensions import db


# NovidadesCarrinho
# tabela que contem as novidades colocadas no carrinho pelo usuário
# id => chave primária
# quantidade => quantidade de novidades colocadas no carrinho 
# preco_total => preço total de todas as novidades colocadas 

class NovidadesCarrinho(db.Model):
        __tablename__ = 'NovidadesCarrinho'
        id = db.Column(db.Integer, primary_key = True)
        nome_novidade = db.Column(db.String(20), nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # novidades carrinho (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # novidades(one) <-> novidades carrinho(many)
        novidades_id = db.Column(db.Integer, db.ForeignKey('novidades.id'))

        def json(self):
                return{
                'nome_novidade':self.nome_novidade,
                'quantidade':self.quantidade,
                'preco_total':self.preco_total
                }