# -*- coding: utf-8 -*-
import logging

from telegram.ext import Updater, Filters, MessageHandler

import config
import util

util.setup_logging()
logger = logging.getLogger(__name__)


def greet(update, context):
    """Sends a greeting message to the user who joined!"""
    welcome_text = "Hallo {}, wilkommen in der Human Bios Entwickler Gruppe!"
    update.message.reply_text(welcome_text.format(update.effective_user.first_name))


updater = Updater(token=config.BOT_TOKEN, use_context=True)

greeting_handler = MessageHandler(Filters.group & Filters.status_update.new_chat_members, greet)
updater.dispatcher.add_handler(greeting_handler)

# Config for webhook - if not set we are using long polling
if config.USE_WEBHOOK:
    updater.start_webhook(listen="127.0.0.1", port=config.WEBHOOK_PORT, url_path=config.BOT_TOKEN, cert=config.CERTPATH, webhook_url=config.WEBHOOK_URL)
    updater.bot.set_webhook(config.WEBHOOK_URL)
else:
    updater.start_polling()

updater.idle()
