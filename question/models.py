from django.db import models


class Question(models.Model):
    """Question or feedback from the feedback form"""
    sender_name = models.CharField(max_length=50, verbose_name='Имя отправителя')
    sender_contact_information = models.CharField(max_length=255, verbose_name='Контактная информация отправителя')
    feedback_subject = models.CharField(max_length=255, verbose_name='Тема обращения')
    feedback_text = models.TextField(verbose_name='Текст обращения')
    is_answered = models.BooleanField(default=False, verbose_name='На вопрос отвечено?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки обращения')
