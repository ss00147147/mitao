# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0004_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=30, verbose_name='\u6807\u9898')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
