# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_created',
            field=models.DateField(default=datetime.datetime(2015, 2, 27, 11, 50, 12, 672000), auto_now_add=True),
            preserve_default=False,
        ),
    ]