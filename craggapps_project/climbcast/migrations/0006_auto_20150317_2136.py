# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0005_userweatherdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userweatherdata',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserWeatherData',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cold_tolerance',
            field=models.CharField(default=b'3', max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='heat_tolerance',
            field=models.CharField(default=b'3', max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mind_windy',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
    ]
