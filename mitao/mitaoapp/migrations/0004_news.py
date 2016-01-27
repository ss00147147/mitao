# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0003_remove_myperson_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
