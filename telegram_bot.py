"""
Módulo responsável por enviar mensagens via Telegram Bot API.
"""

import requests
import logging
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

logger = logging.getLogger(__name__)

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"


def enviar_mensagem(texto: str) -> bool:
    """
    Envia uma mensagem para o seu Telegram via Bot.

    Args:
        texto: Texto da mensagem (suporta Markdown).

    Returns:
        True se enviou com sucesso, False caso contrário.
    """
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown"
    }

    try:
        resposta = requests.post(TELEGRAM_API_URL, json=payload, timeout=10)
        resposta.raise_for_status()
        logger.info("Mensagem enviada ao Telegram com sucesso.")
        return True

    except requests.exceptions.Timeout:
        logger.error("Timeout ao tentar enviar mensagem para o Telegram.")
        return False

    except requests.exceptions.HTTPError as e:
        logger.error(f"Erro HTTP ao enviar para o Telegram: {e.response.text}")
        return False

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de conexão com o Telegram: {e}")
        return False


def testar_conexao() -> bool:
    """
    Testa se o bot está configurado corretamente enviando
    uma mensagem de boas-vindas ao Telegram.
    """
    texto = (
        "✅ *WhatsApp Relay Ativado!*\n"
        "O servidor está online e pronto para repassar mensagens do WhatsApp."
    )
    return enviar_mensagem(texto)
