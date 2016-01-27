# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0020_auto_20160127_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourgroup',
            name='Exclusive',
            field=models.FileField(default='', upload_to='exclusive/%Y/%m/%d/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tourgroup',
            name='Cover',
            field=models.FileField(default='', upload_to='cover/%Y/%m/%d/'),
            preserve_default=True,
        ),
    ]
