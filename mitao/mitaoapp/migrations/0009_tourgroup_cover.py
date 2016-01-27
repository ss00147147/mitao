# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0008_auto_20160123_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourgroup',
            name='Cover',
            field=models.FileField(default='', upload_to='mitaoapp/static/upload/cover/'),
            preserve_default=True,
        ),
    ]
