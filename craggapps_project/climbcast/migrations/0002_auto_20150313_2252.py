# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='area1',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='area2',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='area3',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='area4',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='area5',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='image_medium',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='image_small',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='users',
            field=models.ManyToManyField(to='climbcast.UserProfile', null=True, blank=True),
            preserve_default=True,
        ),
    ]
