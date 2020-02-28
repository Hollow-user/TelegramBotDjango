from telegram import Update
from telegram.ext import CallbackContext

from tgbot.models import Message, Profile
from tgbot.utils.logger import log_errors


@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    # Берем или создаем профиль пользователя
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    # Сохранение сообщения
    message = Message(
        profile=p,
        text=text,
    )
    message.save()

    reply_text = text
    update.message.reply_text(
        text=reply_text
    )


@log_errors
def do_count(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    # Берем или создаем профиль пользователя
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    count = Message.objects.filter(profile=p).count()

    update.message.reply_text(
        text=f'У вас {count} сообщений'
    )
