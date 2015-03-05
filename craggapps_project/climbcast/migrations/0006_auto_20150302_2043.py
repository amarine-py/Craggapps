# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0005_auto_20150302_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craggarea',
            name='area_lat',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=5, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='craggarea',
            name='area_lon',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=5, blank=True),
            preserve_default=True,
        ),
    ]
