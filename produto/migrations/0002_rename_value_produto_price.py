# Generated by Django 5.0.3 on 2024-03-25 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='value',
            new_name='price',
        ),
    ]
