# Generated by Django 3.2 on 2022-12-13 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dollido', '0003_remove_lost_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='lost',
            name='result',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='lost',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
    ]