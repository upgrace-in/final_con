# Generated by Django 3.2.6 on 2021-08-18 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest_app', '0010_auto_20210814_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz_an',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_given', models.TextField(max_length=2000)),
                ('correct_answer', models.TextField(max_length=2000)),
                ('i_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest_app.users_data')),
            ],
        ),
        migrations.CreateModel(
            name='quiz_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_question', models.TextField(max_length=5000)),
                ('hin_question', models.TextField(max_length=5000)),
                ('answer', models.TextField(max_length=2000)),
                ('option1', models.TextField(max_length=2000)),
                ('option2', models.TextField(max_length=2000)),
                ('option3', models.TextField(max_length=2000)),
                ('option4', models.TextField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='quiz',
        ),
        migrations.AddField(
            model_name='quiz_an',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest_app.quiz_question'),
        ),
    ]
