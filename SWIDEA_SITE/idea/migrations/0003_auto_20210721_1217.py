# Generated by Django 3.2.5 on 2021-07-21 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_auto_20210720_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idealist',
            old_name='desc',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='idealist',
            old_name='idea',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='idealist',
            name='dev_tool',
        ),
        migrations.RemoveField(
            model_name='idealist',
            name='photo',
        ),
        migrations.AddField(
            model_name='idealist',
            name='devtool',
            field=models.CharField(blank=True, choices=[('Node.js', 'Node.js'), ('Spring', 'Spring'), ('Django', 'Django'), ('JavaScript', 'JavaScript')], help_text='예상 개발툴', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='idealist',
            name='image',
            field=models.ImageField(blank=True, help_text='대표 사진', null=True, upload_to='idea_image/%Y/%m/%d/'),
        ),
    ]