# Generated by Django 3.2.6 on 2021-08-10 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('pdf', models.FileField(upload_to='static/pdfs')),
            ],
        ),
        migrations.CreateModel(
            name='users_data',
            fields=[
                ('id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mail_id', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=100)),
                ('razorpay_order_id', models.CharField(max_length=1000)),
                ('razorpay_payment_id', models.CharField(max_length=1000)),
                ('razorpay_signature', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='appiled_for',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='static/uploads')),
                ('contest_mdl', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contest_app.contests')),
                ('i_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest_app.users_data')),
            ],
        ),
    ]
