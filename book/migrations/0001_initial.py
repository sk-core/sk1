# Generated by Django 4.2.16 on 2024-10-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='书名')),
                ('description', models.TextField(verbose_name='书籍简介')),
                ('image', models.ImageField(upload_to='book/images/', verbose_name='书籍封面')),
                ('url', models.URLField(blank=True, verbose_name='电子书链接')),
            ],
            options={
                'verbose_name': '读书',
                'verbose_name_plural': '读书',
            },
        ),
    ]
