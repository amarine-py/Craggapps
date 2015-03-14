# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0002_auto_20150313_2252'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CraggUser',
        ),
    ]
