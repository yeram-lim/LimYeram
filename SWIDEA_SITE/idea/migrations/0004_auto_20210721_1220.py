# Generated by Django 3.2.5 on 2021-07-21 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0003_auto_20210721_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idealist',
            name='devtool',
        ),
        migrations.RemoveField(
            model_name='idealist',
            name='image',
        ),
    ]
