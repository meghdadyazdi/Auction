# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-22 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0018_remove_bid_info_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sold',
            field=models.IntegerField(default=0),
        ),
    ]