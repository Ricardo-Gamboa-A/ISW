# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-14 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_galleryphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(null=True),
        ),
    ]