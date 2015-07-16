# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level_rank', models.IntegerField(default=0)),
                ('tray_slots', models.IntegerField(default=8)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(default=0)),
                ('tray_tag', models.CharField(default=None, max_length=20)),
                ('kind', models.CharField(default=None, max_length=20)),
                ('variety', models.CharField(default=None, max_length=20)),
                ('seed_volume', models.IntegerField(default=0)),
                ('supplier', models.CharField(default=None, max_length=20)),
                ('date_seeded', models.DateTimeField(default=None, verbose_name=b'Date_Seeded')),
                ('date_uncovered', models.DateTimeField(default=None, verbose_name=b'Date_Uncovered')),
                ('date_harvested', models.DateTimeField(default=None, verbose_name=b'Date_Harvested')),
                ('level', models.ForeignKey(to='tracking.Level')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_text', models.CharField(max_length=200)),
                ('unit_height', models.IntegerField(default=0)),
                ('unit_length', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='unit',
            field=models.ForeignKey(to='tracking.Unit'),
        ),
    ]
