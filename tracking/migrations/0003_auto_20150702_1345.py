# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20150702_0910'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Building',
            new_name='Farm',
        ),
        migrations.RenameField(
            model_name='farm',
            old_name='building_address',
            new_name='farm_address',
        ),
    ]
