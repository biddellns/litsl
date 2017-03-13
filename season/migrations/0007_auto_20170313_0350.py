# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0006_auto_20161220_0258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['-active']},
        ),
        migrations.AddField(
            model_name='season',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='season',
            name='state',
            field=models.CharField(choices=[('pre', 'Preseason'), ('reg', 'Regular Season'), ('post', 'Playoffs'), ('comp', 'Complete')], default='pre', max_length=4),
            preserve_default=False,
        ),
    ]
