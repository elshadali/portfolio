# Generated by Django 4.2.7 on 2023-11-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_open'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=200, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
