# Generated by Django 2.1.2 on 2018-10-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_auto_20181023_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Hard', 'Hard'), ('Very Hard', 'Very Hard')], default='Easy', max_length=1),
        ),
    ]
