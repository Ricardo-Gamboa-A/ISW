# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-18 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recovery_token',
            field=models.CharField(max_length=128, null=True),
        ),
    ]