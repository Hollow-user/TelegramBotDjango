from django.contrib import admin

from .models import Message, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Профили пользователей Telegram
    """
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Сообщения пользователей Telegram
    """
    pass
