# Generated by Django 3.2 on 2022-12-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apilistid',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
