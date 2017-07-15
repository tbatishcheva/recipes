# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Ingridient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Ingridients_of_recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('count', models.IntegerField()),
                ('ingridient_id', models.ForeignKey(to='recipes.Ingridient')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
                ('description', models.CharField(max_length=63)),
                ('main_img', models.CharField(max_length=63)),
                ('cooking_time', models.IntegerField()),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_time', models.DateTimeField()),
                ('cuisine_id', models.ForeignKey(to='recipes.Cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Set_of_tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('recipe_id', models.ForeignKey(to='recipes.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('img', models.CharField(max_length=255)),
                ('recipe_id', models.ForeignKey(to='recipes.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=31)),
            ],
        ),
        migrations.AddField(
            model_name='set_of_tag',
            name='tag_id',
            field=models.ForeignKey(to='recipes.Tag'),
        ),
        migrations.AddField(
            model_name='ingridients_of_recipe',
            name='measure_id',
            field=models.ForeignKey(to='recipes.Measure'),
        ),
        migrations.AddField(
            model_name='ingridients_of_recipe',
            name='recipe_id',
            field=models.ForeignKey(to='recipes.Recipe'),
        ),
    ]
