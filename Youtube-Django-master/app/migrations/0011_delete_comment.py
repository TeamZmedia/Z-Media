# Generated by Django 4.1.4 on 2023-12-08 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
