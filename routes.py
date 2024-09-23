from flask import request
from app.utils import generate_response
from app import db
from app.vendas.models import Venda, VendaCliente, VendaMercadoria
import logging
from datetime import datetime


def routes(app):
    @app.route("/vendas", methods=["POST"])
    def criar_venda():
        data = request.get_json()
        if not data or not "preco" in data:
            logging.error("Dados inválidos ao tentar criar venda")
            return generate_response({"error": "Preço é obrigatório."}, status=400)

        try:
            nova_venda = Venda(
                preco=data["preco"],
                datavenda=datetime.strptime(
                    data["datavenda"], "%Y-%m-%d") if data.get("datavenda") else None,
                formapag=data.get("formapag"),
            )
            db.session.add(nova_venda)
            db.session.commit()

            if "clientes" in data:
                for id_cliente in data["clientes"]:
                    nova_venda_cliente = VendaCliente(
                        idvenda=nova_venda.idvenda, idcliente=id_cliente)
                    db.session.add(nova_venda_cliente)

            if "mercadorias" in data:
                for item in data["mercadorias"]:
                    nova_venda_mercadoria = VendaMercadoria(
                        idvenda=nova_venda.idvenda, idproduto=item["idproduto"])
                    db.session.add(nova_venda_mercadoria)

            db.session.commit()
            logging.info(f"Venda criada com sucesso: {nova_venda.idvenda}")
            return generate_response(nova_venda.serialize(), status=201, message="Venda criada com sucesso")
        except Exception as e:
            logging.error(f"Erro ao criar venda: {e}")
            return generate_response({"error": "Erro ao criar venda."}, status=500)

    @app.route("/vendas", methods=["GET"])
    def listar_vendas():
        vendas = Venda.query.all()
        return generate_response([venda.serialize() for venda in vendas])

    @app.route("/vendas/<int:id>", methods=["GET"])
    def obter_venda(id):
        venda = Venda.query.get_or_404(id)
        return generate_response(venda.serialize())

    @app.route("/vendas/<int:id>", methods=["PUT"])
    def atualizar_venda(id):
        venda = Venda.query.get_or_404(id)
        data = request.get_json()

        try:
            venda.preco = data.get("preco", venda.preco)
            venda.datavenda = (
                datetime.strptime(data.get(
                    "datavenda"), "%Y-%m-%d") if data.get("datavenda") else venda.datavenda
            )
            venda.formapag = data.get("formapag", venda.formapag)

            db.session.commit()
            logging.info(f"Venda atualizada com sucesso: {venda.idvenda}")
            return generate_response(venda.serialize(), status=200, message="Venda atualizada com sucesso")
        except Exception as e:
            logging.error(f"Erro ao atualizar venda: {e}")
            return generate_response({"error": "Erro ao atualizar venda."}, status=500)

    @app.route("/vendas/<int:id>", methods=["DELETE"])
    def excluir_venda(id):
        venda = Venda.query.get_or_404(id)

        try:
            db.session.delete(venda)
            db.session.commit()
            logging.info(f"Venda excluída com sucesso: {venda.idvenda}")
            return generate_response({}, status=200, message="Venda excluída com sucesso")
        except Exception as e:
            logging.error(f"Erro ao excluir venda: {e}")
            return generate_response({"error": "Erro ao excluir venda."}, status=500)
