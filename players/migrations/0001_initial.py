# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 02:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnet_name', models.CharField(max_length=30)),
                ('bnet_id', models.IntegerField()),
                ('bnet_profile_url', models.URLField()),
                ('sc2_name', models.CharField(max_length=30)),
                ('sc2_id', models.IntegerField()),
                ('league', models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'Gold'), ('P', 'Platinum'), ('D', 'Diamond'), ('M', 'Masters')], max_length=1)),
                ('race', models.CharField(choices=[('P', 'Protoss'), ('T', 'Terran'), ('Z', 'Zerg'), ('R', 'Random')], max_length=1)),
                ('ladder_games_played', models.IntegerField(blank=True, null=True)),
                ('team', models.CharField(max_length=30)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
