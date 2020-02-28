from django.conf import settings
from django.core.management.base import BaseCommand
from telegram import Bot
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram.utils.request import Request

from tgbot.utils import simple_utils


class Command(BaseCommand):
    help = 'Telegram Бот'

    def handle(self, *args, **options):
        # Подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0
        )
        bot = Bot(
            request=request,
            token=settings.BOT_TOKEN,
            base_url=settings.PROXY_URL
        )
        print(bot.get_me())

        # Обработчик сообщений
        updater = Updater(
            bot=bot,
            use_context=True
        )

        message_handler2 = CommandHandler('count', simple_utils.do_count)
        updater.dispatcher.add_handler(message_handler2)

        message_handler = MessageHandler(Filters.text, simple_utils.do_echo)
        updater.dispatcher.add_handler(message_handler)

        # Запустить обработку входящих сообщений

        updater.start_polling()
        updater.idle()
