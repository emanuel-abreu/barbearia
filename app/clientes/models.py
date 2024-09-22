from app import db
from sqlalchemy.orm import relationship


class Cliente(db.Model):
    __tablename__ = "cliente"
    idcliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomecompletocliente = db.Column(db.String(30), nullable=False)
    senha = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(40), nullable=True)
    telefone = db.Column(db.String(15), nullable=True)
    cpf = db.Column(db.String(15), nullable=True)

    agendamentos = relationship("Agendamento", back_populates="cliente")
    vendas = relationship("VendaCliente", back_populates="cliente")

    def serialize(self):
        return {
            "idcliente": self.idcliente,
            "nomecompletocliente": self.nomecompletocliente,
            "senha": self.senha,
            "email": self.email,
            "telefone": self.telefone,
            "cpf": self.cpf,
        }
