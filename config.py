"""
Configurações do WhatsApp Relay.
Preencha as variáveis abaixo com seus dados reais.
"""

import os

# ─────────────────────────────────────────────
# TELEGRAM
# ─────────────────────────────────────────────

# Token do seu bot (gerado pelo @BotFather no Telegram)
# Exemplo: "123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7748514364:AAGEAgHl3bJ9uV6Kn9s_Oce6JiGx5_eM2jE")

# Seu Chat ID pessoal no Telegram
# Para descobrir: acesse https://api.telegram.org/bot<TOKEN>/getUpdates
# após mandar uma mensagem pro seu bot
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "7074510022")

# ─────────────────────────────────────────────
# SEGURANÇA
# ─────────────────────────────────────────────

# Chave secreta para validar que o Macrodroid é quem está enviando
# Crie qualquer string aleatória, ex: "minha-chave-super-secreta-2024"
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "novo-auto-cod-2024")
