# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='craggarea',
            name='cragg_user',
        ),
        migrations.AddField(
            model_name='craggarea',
            name='cragg_users',
            field=models.ManyToManyField(to='climbcast.CraggUser'),
            preserve_default=True,
        ),
    ]
