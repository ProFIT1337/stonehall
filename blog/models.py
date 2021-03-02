from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Post category in blog"""
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг категории')

    def __str__(self):
        return f'Категория {self.name}'

    # def get_absolute_url(self):
    #     return reverse()


class Post(models.Model):
    """Post in blog"""
    category = models.ForeignKey(Category, verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Название поста')
    slug = models.SlugField(unique=True, verbose_name='Слаг поста')
    content = models.TextField(verbose_name='Контент')
    creating_at = models.DateTimeField(auto_created=True, verbose_name='Дата и время создания')
    image = models.ImageField(verbose_name='Заглавная фотография')

    def __str__(self):
        return f'Пост {self.title}'
