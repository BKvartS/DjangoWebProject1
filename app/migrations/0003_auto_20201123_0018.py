# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-22 21:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201120_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 23, 0, 18, 49, 919689), verbose_name='Опубликована'),
        ),
    ]
