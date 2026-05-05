"""
WhatsApp → Telegram Relay
Servidor Flask que recebe webhooks do Macrodroid e repassa para o Telegram.
"""

from flask import Flask, request, jsonify
from telegram_bot import enviar_mensagem
from config import WEBHOOK_SECRET
import logging

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health_check():
    """Rota de verificação — confirma que o servidor está online."""
    return jsonify({"status": "online", "servico": "WhatsApp Relay"}), 200


@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Recebe o POST do Macrodroid com a mensagem do WhatsApp
    e repassa para o Telegram.

    Payload esperado (JSON):
    {
        "secret": "sua_chave_secreta",
        "contato": "Nome do Contato",
        "mensagem": "Texto da mensagem recebida"
    }
    """
    dados = request.get_json(silent=True)

    # Valida se o payload chegou
    if not dados:
        logger.warning("Requisição recebida sem payload JSON.")
        return jsonify({"erro": "Payload JSON ausente"}), 400

    # Valida o secret para evitar requisições não autorizadas
    if dados.get("secret") != WEBHOOK_SECRET:
        logger.warning("Requisição com secret inválido bloqueada.")
        return jsonify({"erro": "Não autorizado"}), 401

    contato = dados.get("contato", "Desconhecido")
    mensagem = dados.get("mensagem", "")

    if not mensagem:
        return jsonify({"erro": "Campo 'mensagem' está vazio"}), 400

    logger.info(f"Mensagem recebida de '{contato}': {mensagem[:50]}...")

    # Formata e envia para o Telegram
    texto_telegram = (
        f"📱 *Mensagem do WhatsApp*\n"
        f"👤 *De:* {contato}\n"
        f"💬 *Mensagem:*\n{mensagem}"
    )

    sucesso = enviar_mensagem(texto_telegram)

    if sucesso:
        return jsonify({"status": "mensagem enviada ao Telegram"}), 200
    else:
        return jsonify({"erro": "Falha ao enviar para o Telegram"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
