# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CraggArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_name', models.CharField(unique=True, max_length=50)),
                ('area_state', models.CharField(max_length=2)),
                ('area_city', models.CharField(max_length=50)),
                ('area_lat', models.DecimalField(null=True, max_digits=7, decimal_places=5, blank=True)),
                ('area_lon', models.DecimalField(null=True, max_digits=8, decimal_places=5, blank=True)),
                ('area_zip', models.CharField(max_length=5, blank=True)),
                ('area_noaa_station_code', models.CharField(max_length=6, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('cover_image', models.ImageField(upload_to=b'cover_images', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CraggUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mp_id', models.CharField(unique=True, max_length=9, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=10, blank=True)),
                ('rating', models.CharField(max_length=15)),
                ('stars', models.CharField(max_length=3, blank=True)),
                ('star_votes', models.CharField(max_length=10, blank=True)),
                ('pitches', models.CharField(max_length=3, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('area1', models.CharField(max_length=50, null=True)),
                ('area2', models.CharField(max_length=50)),
                ('area3', models.CharField(max_length=50)),
                ('area4', models.CharField(max_length=50)),
                ('area5', models.CharField(max_length=50)),
                ('mp_url', models.URLField(unique=True, blank=True)),
                ('image_small_url', models.URLField(null=True, blank=True)),
                ('image_medium_url', models.URLField(null=True, blank=True)),
                ('image_small', models.ImageField(null=True, upload_to=b'')),
                ('image_medium', models.ImageField(null=True, upload_to=b'')),
                ('slug', models.SlugField(unique=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='route',
            name='users',
            field=models.ManyToManyField(to='climbcast.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='craggarea',
            name='cragg_users',
            field=models.ManyToManyField(to='climbcast.UserProfile'),
            preserve_default=True,
        ),
    ]
