# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0006_auto_20150227_1237'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CraggUser',
        ),
    ]
