# Generated by Django 3.0.7 on 2020-06-28 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200626_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='end_date',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='start_date',
            new_name='start_time',
        ),
    ]