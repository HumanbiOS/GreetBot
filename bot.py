# -*- coding: utf-8 -*-
import logging
import os

from telegram.ext import Updater, Filters, MessageHandler

import config
import text
import util

util.setup_logging()
logger = logging.getLogger(__name__)


def greet(update, _context):
    """Sends a greeting message to the user who joined!"""
    new_member = update.message.new_chat_members[0]
    if new_member.language_code == 'de':
        update.message.reply_text(text.WELCOME_TEXT_DE.format(new_member.name))
    else:
        update.message.reply_text(text.WELCOME_TEXT_EN.format(new_member.name))


TOKEN = os.getenv("TOKEN")
ENV = os.getenv("ENV")

updater = Updater(token=TOKEN, use_context=True)

greeting_handler = MessageHandler(Filters.group & Filters.status_update.new_chat_members, greet)
updater.dispatcher.add_handler(greeting_handler)

if ENV == "prod":
    port = int(os.environ.get("PORT", "8443"))
    app_name = os.environ.get("HEROKU_APP_NAME")
    updater.start_webhook(listen="0.0.0.0", port=port, url_path=TOKEN)
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(app_name, TOKEN))
else:
    if config.USE_WEBHOOK:
        updater.start_webhook(listen="127.0.0.1", port=config.WEBHOOK_PORT, url_path=config.BOT_TOKEN,
                              cert=config.CERTPATH,
                              webhook_url=config.WEBHOOK_URL)
        updater.bot.set_webhook(config.WEBHOOK_URL)
    else:
        updater.start_polling()

    updater.idle()
