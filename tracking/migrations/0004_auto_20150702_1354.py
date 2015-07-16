# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_auto_20150702_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='building',
            new_name='farm',
        ),
    ]
