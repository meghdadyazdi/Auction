# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-07 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_bid_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid_info',
            name='highest_bid_user',
            field=models.CharField(default='a', max_length=200),
        ),
    ]