from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Venda(db.Model):
    __tablename__ = "venda"
    idvenda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    datavenda = db.Column(db.Date, nullable=True)
    formapag = db.Column(db.String(20), nullable=True)

    clientes = relationship("VendaCliente", back_populates="venda")
    mercadorias = relationship("VendaMercadoria", back_populates="venda")


def serialize(self):
    return {
        "idvenda": self.idvenda,
        "preco": str(self.preco),
        "datavenda": self.datavenda.strftime("%Y-%m-%d") if self.datavenda else None,
        "formapag": self.formapag,
        "clientes": [cliente.serialize() for cliente in self.clientes],
        "mercadorias": [mercadoria.serialize() for mercadoria in self.mercadorias],
    }


class VendaCliente(db.Model):
    __tablename__ = "vendacliente"
    idvenda = db.Column(db.Integer, ForeignKey(
        "venda.idvenda"), primary_key=True)
    idcliente = db.Column(db.Integer, ForeignKey(
        "cliente.idcliente"), primary_key=True)

    venda = relationship("Venda", back_populates="clientes")
    cliente = relationship("Cliente", back_populates="vendas")

    def serialize(self):
        return {
            "idvenda": self.idvenda,
            "idcliente": self.idcliente,
            "cliente": self.cliente.nome if self.cliente else None,
        }


class VendaMercadoria(db.Model):
    __tablename__ = "vendamercadoria"
    idproduto = db.Column(db.Integer, ForeignKey(
        "produto.idproduto"), primary_key=True)
    idvenda = db.Column(db.Integer, ForeignKey(
        "venda.idvenda"), primary_key=True)

    produto = relationship("Produto", back_populates="vendamercadorias")
    venda = relationship("Venda", back_populates="mercadorias")

    def serialize(self):
        return {
            "idproduto": self.idproduto,
            "idvenda": self.idvenda,
            "produto": self.produto.nomeproduto if self.produto else None,
        }
