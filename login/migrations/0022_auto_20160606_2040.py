# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-07 00:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_auto_20160509_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
