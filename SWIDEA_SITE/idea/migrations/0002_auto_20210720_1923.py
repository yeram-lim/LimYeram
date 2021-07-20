# Generated by Django 3.2.5 on 2021-07-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.CharField(help_text='아이디어명', max_length=100)),
                ('photo', models.ImageField(blank=True, help_text='대표 사진', null=True, upload_to='')),
                ('desc', models.TextField(blank=True, help_text='아이디어 설명')),
                ('interest', models.IntegerField(help_text='아이디어 관심도')),
                ('dev_tool', models.CharField(blank=True, choices=[('Node.js', 'Node.js'), ('Spring', 'Spring')], help_text='예상 개발툴', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='idea_list',
        ),
    ]
