# Generated by Django 3.1.7 on 2021-03-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210314_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
