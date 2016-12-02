# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GroupRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_players', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('season_number', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='groupround',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_rounds', to='season.Season'),
        ),
        migrations.AddField(
            model_name='group',
            name='group_round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='season.GroupRound'),
        ),
        migrations.AddField(
            model_name='group',
            name='players',
            field=models.ManyToManyField(to='players.Player'),
        ),
    ]
