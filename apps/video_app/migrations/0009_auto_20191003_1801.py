# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-03 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0008_auto_20191003_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='course_app.Course'),
        ),
    ]
