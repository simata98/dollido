# Generated by Django 3.2 on 2022-12-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dollido', '0004_auto_20221213_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiListId',
            fields=[
                ('atcId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('fdPrdtNm', models.CharField(default='', max_length=500, null=True)),
                ('fdFilePathImg', models.CharField(max_length=300)),
                ('fdSbjt', models.CharField(max_length=500)),
                ('depPlace', models.CharField(max_length=30)),
                ('fdYmd', models.DateField(max_length=10, null=True)),
                ('category', models.CharField(max_length=20)),
                ('clrNm', models.CharField(max_length=10)),
            ],
        ),
    ]
