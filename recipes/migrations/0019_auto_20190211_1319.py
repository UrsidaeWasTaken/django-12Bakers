# Generated by Django 2.1.2 on 2019-02-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_auto_20181102_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='thumbnail',
            field=models.ImageField(default='no_image.png', upload_to='recipes'),
        ),
    ]