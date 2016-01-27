# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0002_auto_20151209_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myperson',
            name='age',
        ),
    ]
