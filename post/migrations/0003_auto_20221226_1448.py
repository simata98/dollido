# Generated by Django 3.2 on 2022-12-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_dollidolstid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='dollidolstid',
            name='clrNm',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='dollidolstid',
            name='create_date',
            field=models.DateTimeField(default='2022-12-26 14:48:04'),
        ),
        migrations.AlterField(
            model_name='dollidolstid',
            name='lstFilePathImg',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='사진 등록'),
        ),
    ]
