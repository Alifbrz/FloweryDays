# Generated by Django 3.0.8 on 2021-01-08 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210106_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='flower',
            old_name='flower_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_name',
            new_name='name',
        ),
    ]
