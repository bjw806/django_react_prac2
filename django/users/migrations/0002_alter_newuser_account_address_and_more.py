# Generated by Django 4.0.4 on 2022-05-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='account_address',
            field=models.BigIntegerField(default='51239200', unique=True, verbose_name='account address'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='account_money',
            field=models.BigIntegerField(default=0, verbose_name='account money'),
        ),
    ]
