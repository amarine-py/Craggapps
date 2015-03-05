# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('climbcast', '0003_auto_20150228_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cragguser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='cragguser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='cragguser',
            name='user_created',
        ),
        migrations.RemoveField(
            model_name='cragguser',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='cragguser',
            name='user_password',
        ),
        migrations.RemoveField(
            model_name='cragguser',
            name='username',
        ),
        migrations.AddField(
            model_name='cragguser',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cragguser',
            name='user',
            field=models.OneToOneField(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
