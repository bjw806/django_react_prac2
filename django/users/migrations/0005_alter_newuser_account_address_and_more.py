# Generated by Django 4.0.4 on 2022-05-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_newuser_account_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='account_address',
            field=models.BigIntegerField(default='72874160', unique=True, verbose_name='account address'),
        ),
        migrations.AlterField(
            model_name='transferreport',
            name='receive_account',
            field=models.BigIntegerField(verbose_name='receive account'),
        ),
        migrations.AlterField(
            model_name='transferreport',
            name='send_account',
            field=models.BigIntegerField(verbose_name='send account'),
        ),
    ]
