# Generated by Django 3.2 on 2022-12-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_dollidolstid_clrnm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollidolstid',
            name='lstFilePathImg',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='사진 등록'),
        ),
    ]