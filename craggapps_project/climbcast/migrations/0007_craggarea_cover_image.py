# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0006_auto_20150302_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='craggarea',
            name='cover_image',
            field=models.ImageField(upload_to=b'cover_images', blank=True),
            preserve_default=True,
        ),
    ]
