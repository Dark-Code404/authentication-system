# Generated by Django 5.1.6 on 2025-02-12 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0006_alter_todo_options_alter_todo_complete_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='content',
            new_name='description',
        ),
    ]
