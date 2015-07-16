# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='building',
            field=models.ForeignKey(default=None, to='tracking.Building'),
        ),
        migrations.AlterField(
            model_name='building',
            name='building_address',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='position',
            name='date_harvested',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='date_seeded',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='date_uncovered',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='kind',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='position',
            name='supplier',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='position',
            name='tray_tag',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='position',
            name='variety',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_text',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
