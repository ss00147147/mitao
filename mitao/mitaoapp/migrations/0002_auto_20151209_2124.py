# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myperson',
            old_name='aname',
            new_name='password',
        ),
    ]
