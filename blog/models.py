from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from markdown import markdown


class Post(models.Model):
    """Post in blog"""
    title = models.CharField(max_length=255, verbose_name='Название поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    image = models.ImageField(verbose_name='Заглавная фотография')
    is_on_main_page = models.BooleanField(default=False, verbose_name='Должен ли пост отображаться на главной?')
    short_description = models.CharField(max_length=100, verbose_name='Короткое описание для отображения в некоторых '
                                                                      'местах')
    content = models.TextField(verbose_name='Полное описание работы')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Пост {self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
