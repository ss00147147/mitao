# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0019_auto_20160126_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourgroup',
            name='Cover',
            field=models.FileField(upload_to='cover/%Y/%m/%d/'),
            preserve_default=True,
        ),
    ]
