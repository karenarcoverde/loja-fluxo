from app.extensions import db

# Novidades
# tabela que contem as informações sobre todas novidades
# id => chave primária

class Novidades(db.Model):
        __tablename__ = 'novidades'
        id = db.Column(db.Integer, primary_key = True)
        cor = db.Column(db.String(10), nullable = False)
        modelo = db.Column(db.String(20), nullable = False)
        marca = db.Column(db.String(20), nullable = False)
        ano_fabricacao = db.Column(db.Integer, nullable = False)
        motor = db.Column(db.String(10), nullable = False)
        estoque = db.Column(db.Integer, nullable = False)
        preco = db.Column(db.Integer, nullable = False)
        nacional = db.Column(db.Boolean, nullable = False)
        importada = db.Column(db.Boolean, nullable = False)

        # novidades(one) <-> novidades carrinho(many)
        novidades_carrinho = db.relationship('NovidadesCarrinho', backref = 'novidadesCarrinho')

        def json(self):
                return{
                'cor':self.cor,
                'modelo':self.modelo,
                'marca':self.marca,
                'ano_fabricacao':self.ano_fabricacao,
                'motor':self.motor,      
                'estoque':self.estoque,
                'preco':self.preco,
                'nacional':self.nacional,
                'importada':self.importada
                }