# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-08 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0022_auto_20200606_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]