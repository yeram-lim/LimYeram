# Generated by Django 3.2.5 on 2021-07-25 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piro', '0003_auto_20210725_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
