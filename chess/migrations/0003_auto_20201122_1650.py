# Generated by Django 3.1.2 on 2020-11-22 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chess', '0002_auto_20201101_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='buyers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Покупатели'),
        ),
        migrations.AddField(
            model_name='videos',
            name='buyers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Покупатели'),
        ),
    ]
