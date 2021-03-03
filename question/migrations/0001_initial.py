# Generated by Django 3.1.7 on 2021-03-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50, verbose_name='Имя отправителя')),
                ('sender_contact_information', models.CharField(max_length=255, verbose_name='Контактная информация отправителя')),
                ('feedback_subject', models.CharField(max_length=255, verbose_name='Тема обращения')),
                ('feedback_text', models.TextField(verbose_name='Текст обращения')),
                ('is_answered', models.BooleanField(default=False, verbose_name='На вопрос отвечено?')),
            ],
        ),
    ]
