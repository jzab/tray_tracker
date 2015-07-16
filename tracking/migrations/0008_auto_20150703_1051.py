# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0007_auto_20150702_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='farm',
        ),
        migrations.AlterField(
            model_name='position',
            name='date_harvested',
            field=models.DateTimeField(null=True, verbose_name=b'Date Harvested'),
        ),
        migrations.AlterField(
            model_name='position',
            name='date_seeded',
            field=models.DateTimeField(null=True, verbose_name=b'Date Seeded'),
        ),
        migrations.AlterField(
            model_name='position',
            name='date_uncovered',
            field=models.DateTimeField(null=True, verbose_name=b'Date Uncovered'),
        ),
    ]
