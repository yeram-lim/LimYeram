# Generated by Django 3.2.5 on 2021-07-21 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0005_auto_20210721_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='idealist',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 21, 12, 27, 37, 125791)),
        ),
    ]
