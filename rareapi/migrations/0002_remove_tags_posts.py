# Generated by Django 3.2.9 on 2021-11-17 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='posts',
        ),
    ]
