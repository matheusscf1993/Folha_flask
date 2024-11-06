from flask import request, jsonify
from datetime import datetime
from models.ponto import Ponto
from database.session import db

def register_routes(app):

    # Rota para registrar entrada
    @app.route('/ponto/entrada', methods=['POST'])
    def registrar_entrada():
        dados = request.get_json()
        usuario = dados.get('usuario')

        if not usuario:
            return jsonify({"error": "Usuário é obrigatório"}), 400

        novo_ponto = Ponto(usuario=usuario, horario_entrada=datetime.utcnow(), action="entrada")
        db.session.add(novo_ponto)
        db.session.commit()

        return jsonify({"message": "Entrada registrada com sucesso"}), 201

    # Rota para registrar saída
    @app.route('/ponto/saida/<int:ponto_id>', methods=['POST'])
    def registrar_saida(ponto_id):
        ponto = Ponto.query.get(ponto_id)

        if not ponto:
            return jsonify({"error": "Registro de entrada não encontrado"}), 404
        if ponto.horario_saida:
            return jsonify({"error": "Saída já registrada para este ponto"}), 400

        ponto.horario_saida = datetime.utcnow()
        db.session.commit()

        return jsonify({"message": "Saída registrada com sucesso"}), 200

    # Nova Rota para registrar ponto externo (dados enviados do FastAPI)
    @app.route('/ponto/externo', methods=['POST'])
    def registrar_ponto_externo():
        dados = request.get_json()
        usuario = dados.get('usuario')
        horario_entrada = dados.get('hora_entrada')
        horario_saida = dados.get('hora_saida')

        if not usuario:
            return jsonify({"error": "Usuário é obrigatório"}), 400

        novo_ponto = Ponto(usuario=usuario, horario_entrada=horario_entrada, horario_saida=horario_saida, action="externo")
        db.session.add(novo_ponto)
        db.session.commit()

        return jsonify({"message": "Ponto registrado com sucesso"}), 201
