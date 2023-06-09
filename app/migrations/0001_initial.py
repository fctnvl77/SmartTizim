# Generated by Django 4.2 on 2023-04-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asosiy_rasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm1', models.ImageField(upload_to='jamoa_rasm')),
                ('rasm2', models.ImageField(upload_to='jamoa_rasm')),
                ('rasm3', models.ImageField(upload_to='jamoa_rasm')),
            ],
        ),
        migrations.CreateModel(
            name='Boglanish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomer', models.IntegerField()),
                ('link', models.CharField(max_length=100)),
                ('joy_nomi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jamoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='jamoa_rasm')),
                ('rasm1', models.ImageField(upload_to='jamoa_rasm')),
                ('rasm2', models.ImageField(upload_to='jamoa_rasm')),
                ('rasm3', models.ImageField(upload_to='jamoa_rasm')),
                ('jamoa_haqida', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Malumot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malumot', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('soni', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('malumot', models.TextField()),
                ('rasm', models.ImageField(upload_to='jamoa_rasm')),
            ],
        ),
        migrations.CreateModel(
            name='Xizmatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='jamoa_rasm')),
                ('rasm2', models.ImageField(upload_to='jamoa_rasm')),
            ],
        ),
        migrations.CreateModel(
            name='Xususiyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('rasm', models.ImageField(upload_to='jamoa_rasm')),
            ],
        ),
    ]
