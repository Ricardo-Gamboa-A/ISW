# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-08 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='working',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.FileField(max_length=500, null=True, upload_to='static/webpage/images/members/'),
        ),
    ]
