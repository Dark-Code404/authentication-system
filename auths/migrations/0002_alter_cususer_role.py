# Generated by Django 5.1.6 on 2025-02-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cususer',
            name='role',
            field=models.CharField(choices=[('role1', 'Admin user'), ('role2', 'Regular user')], default='role1', max_length=100),
        ),
    ]
