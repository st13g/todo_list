# Generated by Django 3.0.5 on 2020-04-12 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date',
            new_name='datet',
        ),
    ]
