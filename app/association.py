from app.extensions import db

association_pedidos_carroscarrinho = db.Table('association_pedidos_carroscarrinho',db.Model.metadata,
                                        db.Column('carroscarrinho',db.Integer, db.ForeignKey('carroscarrinho.id')),
                                        db.Column('pedidos',db.Integer,db.ForeignKey('pedidos.id')))

association_pedidos_motoscarrinho = db.Table('association_pedidos_motoscarrinho',db.Model.metadata,
                                        db.Column('motoscarrinho',db.Integer, db.ForeignKey('motoscarrinho.id')),
                                        db.Column('pedidos',db.Integer,db.ForeignKey('pedidos.id')))
