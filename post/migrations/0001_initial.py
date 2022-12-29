# Generated by Django 3.2 on 2022-12-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('upper_category', models.CharField(max_length=20)),
                ('middle_category', models.CharField(max_length=20)),
                ('lower_category', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DollidoLstId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lstPrdtNm', models.CharField(blank=True, max_length=200, null=True, verbose_name='습득물 이름')),
                ('lstFilePathImg', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='사진 등록')),
                ('lstcontent', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='특이사항')),
                ('lstYmd', models.DateField(blank=True, max_length=10, null=True)),
                ('lstPlace', models.CharField(blank=True, max_length=200, null=True)),
                ('create_date', models.DateTimeField(default='2022-12-27 11:05:20')),
                ('find_status', models.BooleanField(default=False)),
                ('clrNm', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': '돌리도 게시판',
            },
        ),
    ]
