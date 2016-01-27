# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('aname', models.CharField(max_length=30, verbose_name='\u5916\u53f7')),
                ('age', models.IntegerField(verbose_name='\u5e74\u9f84')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
