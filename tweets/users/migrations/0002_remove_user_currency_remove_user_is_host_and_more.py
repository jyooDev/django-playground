# Generated by Django 5.1.1 on 2024-09-28 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_host',
        ),
        migrations.RemoveField(
            model_name='user',
            name='language',
        ),
    ]
