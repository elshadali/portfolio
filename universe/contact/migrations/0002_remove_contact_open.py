# Generated by Django 4.2.2 on 2023-11-22 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='open',
        ),
    ]
