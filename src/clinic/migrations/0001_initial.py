# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('sorder', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('sorder', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinic.Speciality'),
        ),
    ]
