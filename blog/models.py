from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Post in blog"""
    title = models.CharField(max_length=255, verbose_name='Название поста')
    content = models.TextField(verbose_name='Контент')
    creating_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    image = models.ImageField(verbose_name='Заглавная фотография')
    is_on_main_page = models.BooleanField(default=False, verbose_name='Должен ли пост отображаться на главной?')
    short_description = models.CharField(max_length=100, verbose_name='Короткое описание для отображения в некоторых '
                                                                      'местах')

    def __str__(self):
        return f'Пост {self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
