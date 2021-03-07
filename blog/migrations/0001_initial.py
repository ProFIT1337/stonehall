# Generated by Django 3.1.7 on 2021-03-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название поста')),
                ('content', models.TextField(verbose_name='Контент')),
                ('creating_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('image', models.ImageField(upload_to='', verbose_name='Заглавная фотография')),
                ('is_on_main_page', models.BooleanField(default=False, verbose_name='Должен ли пост отображаться на главной?')),
                ('short_description', models.CharField(max_length=100, verbose_name='Короткое описание для отображения в некоторых местах')),
            ],
        ),
    ]
