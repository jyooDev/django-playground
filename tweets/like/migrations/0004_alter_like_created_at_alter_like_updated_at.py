# Generated by Django 5.1.1 on 2024-09-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0003_alter_like_created_at_alter_like_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_comment='creation date and time'),
        ),
        migrations.AlterField(
            model_name='like',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_comment='last update date and time'),
        ),
    ]
