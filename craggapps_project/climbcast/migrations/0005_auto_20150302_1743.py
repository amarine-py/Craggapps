# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('climbcast', '0004_auto_20150302_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cragguser',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='cragguser',
            name='user',
        ),
        migrations.AddField(
            model_name='cragguser',
            name='username',
            field=models.CharField(default='', unique=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='craggarea',
            name='cragg_users',
            field=models.ManyToManyField(to='climbcast.UserProfile'),
            preserve_default=True,
        ),
    ]
