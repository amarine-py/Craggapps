# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CraggArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_name', models.CharField(unique=True, max_length=50)),
                ('area_state', models.CharField(max_length=2)),
                ('area_city', models.CharField(max_length=50)),
                ('area_lat', models.DecimalField(max_digits=7, decimal_places=5)),
                ('area_lon', models.DecimalField(max_digits=8, decimal_places=5)),
                ('area_zip', models.CharField(max_length=5)),
                ('area_noaa_station_code', models.CharField(max_length=6)),
                ('area_current_temp_yahoo_c', models.DecimalField(max_digits=5, decimal_places=2)),
                ('area_current_temp_yahoo_f', models.DecimalField(max_digits=5, decimal_places=2)),
                ('area_current_temp_weathercom_c', models.DecimalField(max_digits=5, decimal_places=2)),
                ('area_current_temp_weathercom_f', models.DecimalField(max_digits=5, decimal_places=2)),
                ('area_current_temp_noaa_c', models.DecimalField(max_digits=5, decimal_places=2)),
                ('area_current_temp_noaa_f', models.DecimalField(max_digits=5, decimal_places=2)),
                ('area_humidity_yahoo', models.PositiveSmallIntegerField()),
                ('area_humidity_weathercom', models.PositiveSmallIntegerField()),
                ('area_humidity_noaa', models.PositiveSmallIntegerField()),
                ('area_pressure_yahoo_mb', models.DecimalField(max_digits=6, decimal_places=2)),
                ('area_pressure_weathercom_mb', models.DecimalField(max_digits=6, decimal_places=2)),
                ('area_pressure_noaa_mb', models.DecimalField(max_digits=6, decimal_places=2)),
                ('area_wind_speed_yahoo_kmh', models.PositiveSmallIntegerField()),
                ('area_wind_speed_weathercom_kmh_string', models.CharField(max_length=15)),
                ('area_wind_speed_noaa_mph', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CraggUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(unique=True, max_length=255)),
                ('user_password', models.CharField(max_length=50)),
                ('user_created', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='craggarea',
            name='cragg_user',
            field=models.ForeignKey(to='climbcast.CraggUser'),
            preserve_default=True,
        ),
    ]
