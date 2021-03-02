from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Post category in blog"""
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return f'Категория {self.name}'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})


class Post(models.Model):
    """Post in blog"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Название поста')
    content = models.TextField(verbose_name='Контент')
    creating_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    image = models.ImageField(verbose_name='Заглавная фотография')

    def __str__(self):
        return f'Пост {self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
