# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-25 00:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0002_auto_20190625_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='users_who_completed',
            new_name='users_completed',
        ),
    ]
