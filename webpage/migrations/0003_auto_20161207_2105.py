# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-08 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_auto_20161207_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='english_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='spanish_name',
            field=models.CharField(max_length=80),
        ),
    ]
