# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20150702_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='farm',
        ),
    ]
