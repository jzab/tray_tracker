# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_remove_unit_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='farm',
            field=models.ForeignKey(to='tracking.Farm', null=True),
        ),
    ]
