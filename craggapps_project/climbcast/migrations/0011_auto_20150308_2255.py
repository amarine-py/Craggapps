# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0010_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='area1',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='image_medium',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='image_medium_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='image_small',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='image_small_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
