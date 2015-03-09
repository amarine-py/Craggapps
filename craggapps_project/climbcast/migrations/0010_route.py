# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbcast', '0009_auto_20150306_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mp_id', models.CharField(unique=True, max_length=9)),
                ('name', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=10, blank=True)),
                ('rating', models.CharField(max_length=15)),
                ('stars', models.CharField(max_length=3, blank=True)),
                ('star_votes', models.CharField(max_length=10, blank=True)),
                ('pitches', models.CharField(max_length=3, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('area1', models.CharField(max_length=50)),
                ('area2', models.CharField(max_length=50)),
                ('area3', models.CharField(max_length=50)),
                ('area4', models.CharField(max_length=50)),
                ('area5', models.CharField(max_length=50)),
                ('mp_url', models.URLField(unique=True, blank=True)),
                ('image_small_url', models.URLField(blank=True)),
                ('image_medium_url', models.URLField(blank=True)),
                ('image_small', models.ImageField(upload_to=b'')),
                ('image_medium', models.ImageField(upload_to=b'')),
                ('slug', models.SlugField(unique=True)),
                ('users', models.ManyToManyField(to='climbcast.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
