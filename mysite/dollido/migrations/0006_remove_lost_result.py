# Generated by Django 3.2 on 2022-12-13 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dollido', '0005_apilistid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lost',
            name='result',
        ),
    ]