# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0017_auto_20160126_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourgroup',
            name='Cover',
            field=models.ImageField(upload_to='/cover/'),
            preserve_default=True,
        ),
    ]
