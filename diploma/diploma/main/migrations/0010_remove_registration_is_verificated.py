# Generated by Django 4.1.3 on 2023-01-25 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_registration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='is_verificated',
        ),
    ]
