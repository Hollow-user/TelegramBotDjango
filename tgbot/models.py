from django.db import models


class Profile(models.Model):
    """
    Профили пользователей Telegram
    """
    external_id = models.PositiveIntegerField('ID пользователя Telegram', unique=True)
    name = models.CharField('Имя пользователя Telegram', max_length=150)

    def __str__(self):
        return f'ID({self.external_id}) {self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    """
    Сообщения пользователей
    """
    profile = models.ForeignKey(to='tgbot.Profile', on_delete=models.PROTECT, verbose_name='Профиль пользователя')
    text = models.TextField('Текст сообщения')
    created_at = models.DateTimeField('Время получения', auto_now_add=True)

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
