# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('climbcast', '0003_delete_cragguser'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteTick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_tick', models.DateField()),
                ('user_star_vote', models.CharField(max_length=3)),
                ('ascent_style', models.CharField(max_length=15)),
                ('difficulty_vote', models.CharField(max_length=15, null=True, blank=True)),
                ('route', models.ForeignKey(to='climbcast.Route')),
                ('user_tick', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='route',
            name='users',
        ),
    ]
