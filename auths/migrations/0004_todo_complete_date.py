# Generated by Django 5.1.6 on 2025-02-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0003_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='complete_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
