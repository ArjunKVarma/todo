# Generated by Django 5.0.5 on 2024-05-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_todo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
