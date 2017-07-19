# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='main_img',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
