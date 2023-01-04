# Generated by Django 3.2 on 2023-01-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat_info',
            fields=[
                ('date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('lost112_wallet_cnt', models.IntegerField()),
                ('lost112_phone_cnt', models.IntegerField()),
                ('dollido_wallet_cnt', models.IntegerField()),
                ('dollido_phone_cnt', models.IntegerField()),
                ('total_cnt', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='dollidolstid',
            name='create_date',
            field=models.DateTimeField(default='2023-01-04 10:20:57'),
        ),
    ]