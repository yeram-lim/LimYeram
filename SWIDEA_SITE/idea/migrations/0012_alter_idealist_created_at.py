# Generated by Django 3.2.5 on 2021-07-21 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0011_auto_20210721_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idealist',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 22, 1, 4, 53, 236894)),
        ),
    ]
