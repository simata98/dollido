# Generated by Django 3.2 on 2023-01-05 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_dollidolstid_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollidolstid',
            name='create_date',
            field=models.DateTimeField(default='2023-01-05 03:00:11'),
        ),
    ]
