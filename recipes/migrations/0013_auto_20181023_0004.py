# Generated by Django 2.1.2 on 2018-10-22 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_auto_20181021_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Hard', 'Hard'), ('Very Hard', 'Very Hard')], default='Easy', max_length=1),
        ),
    ]
