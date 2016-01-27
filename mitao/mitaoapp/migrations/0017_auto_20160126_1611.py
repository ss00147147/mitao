# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0016_auto_20160126_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourgroup',
            name='Cover',
            field=models.ImageField(upload_to='cover/%Y/%m/%d/'),
            preserve_default=True,
        ),
    ]
