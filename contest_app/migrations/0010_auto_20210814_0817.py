# Generated by Django 3.2.6 on 2021-08-14 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest_app', '0009_auto_20210814_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sloka',
            name='eng_audio',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='sloka',
            name='hin_audio',
            field=models.TextField(max_length=1000),
        ),
    ]