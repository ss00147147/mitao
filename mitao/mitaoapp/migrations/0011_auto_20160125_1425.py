# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitaoapp', '0010_auto_20160125_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourgroup',
            name='Cover',
            field=models.FileField(default='', upload_to='mitaoapp/static/upload/cover/Y/%m/%d/', max_length=255, verbose_name='\u5c01\u9762'),
            preserve_default=True,
        ),
    ]
