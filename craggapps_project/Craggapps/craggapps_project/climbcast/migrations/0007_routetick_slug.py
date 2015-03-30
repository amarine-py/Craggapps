# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0006_auto_20150317_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='routetick',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
            preserve_default=True,
        ),
    ]
