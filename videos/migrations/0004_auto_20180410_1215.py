# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20180409_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
