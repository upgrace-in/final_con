# Generated by Django 3.2.6 on 2021-08-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appiled_for',
            name='uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
