# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['sorder']},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'ordering': ['sorder']},
        ),
    ]
