# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-07 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_auto_20200507_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
