# Generated by Django 5.1 on 2024-12-26 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0010_alter_works_screenshots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='videos',
        ),
    ]
