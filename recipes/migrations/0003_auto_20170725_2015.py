# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20170725_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientsofrecipe',
            old_name='ingridient_id',
            new_name='ingredient_id',
        ),
    ]
