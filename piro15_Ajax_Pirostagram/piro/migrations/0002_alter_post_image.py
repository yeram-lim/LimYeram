# Generated by Django 3.2.5 on 2021-07-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image/%Y/%m/%d/', verbose_name='사진'),
        ),
    ]
