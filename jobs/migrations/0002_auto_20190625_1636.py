# Generated by Django 2.0.2 on 2019-06-25 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobsConfig',
            new_name='Job',
        ),
    ]