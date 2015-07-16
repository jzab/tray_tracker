# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0006_unit_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='farm',
            field=models.ForeignKey(to='tracking.Farm', null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='unit',
            field=models.ForeignKey(to='tracking.Unit', null=True),
        ),
    ]
