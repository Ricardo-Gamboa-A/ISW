# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-20 20:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0002_forum_forumcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='title_slug',
            new_name='slug',
        ),
    ]
