# Generated by Django 3.2.6 on 2021-08-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest_app', '0007_auto_20210810_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_content', models.TextField(max_length=10000)),
            ],
        ),
    ]
