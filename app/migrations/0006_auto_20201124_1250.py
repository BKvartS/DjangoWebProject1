# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-24 09:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201124_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 24, 12, 50, 52, 488637), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 24, 12, 50, 52, 489561), verbose_name='Дата'),
        ),
    ]