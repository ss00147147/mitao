# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0005_tourgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourgroup',
            name='Abstract',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6458\u8981'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tourgroup',
            name='Description',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u63cf\u8ff0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tourgroup',
            name='Notice',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u6ce8\u610f\u4e8b\u9879'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tourgroup',
            name='TripMode',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u884c\u7a0b\u5b89\u6392'),
            preserve_default=True,
        ),
    ]
