# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161213_1224'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set([('title', 'author')]),
        ),
    ]
