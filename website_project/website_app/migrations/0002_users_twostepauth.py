# Generated by Django 5.1 on 2024-09-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='twostepauth',
            field=models.BooleanField(default=False, verbose_name='2 step authentication'),
        ),
    ]
