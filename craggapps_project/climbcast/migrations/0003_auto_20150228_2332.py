# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0002_auto_20150228_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='craggarea',
            name='area_current_temp_noaa_c',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_current_temp_noaa_f',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_current_temp_weathercom_c',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_current_temp_weathercom_f',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_current_temp_yahoo_c',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_current_temp_yahoo_f',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_humidity_noaa',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_humidity_weathercom',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_humidity_yahoo',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_pressure_noaa_mb',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_pressure_weathercom_mb',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_pressure_yahoo_mb',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_wind_speed_noaa_mph',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_wind_speed_weathercom_kmh_string',
        ),
        migrations.RemoveField(
            model_name='craggarea',
            name='area_wind_speed_yahoo_kmh',
        ),
        migrations.AlterField(
            model_name='craggarea',
            name='area_lat',
            field=models.DecimalField(max_digits=7, decimal_places=5, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='craggarea',
            name='area_lon',
            field=models.DecimalField(max_digits=8, decimal_places=5, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='craggarea',
            name='area_noaa_station_code',
            field=models.CharField(max_length=6, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='craggarea',
            name='area_zip',
            field=models.CharField(max_length=5, blank=True),
            preserve_default=True,
        ),
    ]
