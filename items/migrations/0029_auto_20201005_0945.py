# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-10-05 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0028_auto_20201005_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
