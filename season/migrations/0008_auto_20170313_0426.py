# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0007_auto_20170313_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season_number',
            field=models.IntegerField(unique=True),
        ),
    ]