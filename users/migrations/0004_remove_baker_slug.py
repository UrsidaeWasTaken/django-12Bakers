# Generated by Django 2.1.2 on 2019-02-11 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190211_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baker',
            name='slug',
        ),
    ]
