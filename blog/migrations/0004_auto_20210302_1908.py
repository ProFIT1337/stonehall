# Generated by Django 3.1.7 on 2021-03-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210302_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_on_main_page',
            field=models.BooleanField(default=False, verbose_name='Должен ли пост отображаться на главной?'),
        ),
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(default=True, max_length=100, verbose_name='Короткое описание для отображения в некоторых местах'),
            preserve_default=False,
        ),
    ]
