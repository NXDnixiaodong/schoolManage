# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-18 00:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2018, 10, 18, 8, 33, 22, 658000)),
        ),
    ]