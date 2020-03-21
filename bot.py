# -*- coding: utf-8 -*-
import logging
import os

from telegram.ext import Updater, Filters, MessageHandler

import config
import util

util.setup_logging()
logger = logging.getLogger(__name__)

welcome_text = "Hallo {}, " \
               "schoen, dass Du hier bist.\n" \
               "Wir wollen Menschen in Not mit Aerzten oder Psychologen via Chat-bot zusammen bringen. Eine Art bedarfsorientiertes Corona-Chat-Roulette.\n" \
               "- Ein Patient in Indien kann vielleicht im Moment keinen Arzt bei sich kontaktieren und nutzt unseren Bot, um mit einem Arzt in Italien zu sprechen\n" \
               "- Ein Arzt, der psychisch ueberfordert ist, muss vielleicht kurz mit einem Psychologen sprechen\n" \
               "Im ersten Schritt, wollen wir einfach einen Bot bauen, der anhand von zwei Fragen, die Person entweder als \"medizinischen Bedarf\" oder als \"psychologischen Bedarf\" einstuft.\n" \
               "Eine kurze Beschreibung findest Du hier https://humanbios.org/#/\n" \
               "Eine Spec findest Du hier https://hackmd.io/p0vKHdtAR4C1ygXadeTncA?view\n" \
               "Sprich gerne @TobiasHeldt an, wenn Du mitmachen willst.\n\n" \
               "Hi {}, " \
               "nice that you're here.\n" \
               "We want to bring people in need together with doctors or psychologists via a telegram chat bot. Some kind of need-based corona chat roulette.\n" \
               "- A patient in India may be unable to contact a doctor at the moment and is using our bot to speak to a doctor in Italy\n" \
               "- A doctor who is mentally overwhelmed may need to speak to a psychologist briefly\n" \
               "In the first step, we simply want to build a bot that, based on two questions, classifies the person as either \"medical need\" or \"psychological need\".\n" \
               "You can find a short description here https://humanbios.org/#/\n" \
               "You can find a spec here https://hackmd.io/p0vKHdtAR4C1ygXadeTncA?view\n" \
               "Talk to @TobiasHeldt if you want to join.\n"


def greet(update, _context):
    """Sends a greeting message to the user who joined!"""
    new_member_name = update.message.new_chat_members[0].name
    update.message.reply_text(welcome_text.format(new_member_name, new_member_name))


updater = Updater(token=os.getenv("TOKEN"), use_context=True)

greeting_handler = MessageHandler(Filters.group & Filters.status_update.new_chat_members, greet)
updater.dispatcher.add_handler(greeting_handler)

# Config for webhook - if not set we are using long polling
if config.USE_WEBHOOK:
    updater.start_webhook(listen="127.0.0.1", port=config.WEBHOOK_PORT, url_path=config.BOT_TOKEN, cert=config.CERTPATH,
                          webhook_url=config.WEBHOOK_URL)
    updater.bot.set_webhook(config.WEBHOOK_URL)
else:
    updater.start_polling()

updater.idle()
