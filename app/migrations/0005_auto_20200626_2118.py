# Generated by Django 3.0.7 on 2020-06-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200626_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=2, null=True),
        ),
    ]
