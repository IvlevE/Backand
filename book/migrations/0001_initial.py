# Generated by Django 4.1.7 on 2023-03-09 02:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20, verbose_name='last name')),
                ('first_name', models.CharField(max_length=20, verbose_name='first name')),
                ('mid_name', models.CharField(blank=True, max_length=20, verbose_name='mid name')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='book name')),
                ('publickator', models.CharField(max_length=50, verbose_name='Izdatel')),
                ('relize_date', models.DateField(default=datetime.date(2023, 3, 9), verbose_name='relize')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author', verbose_name='Author')),
            ],
        ),
    ]
