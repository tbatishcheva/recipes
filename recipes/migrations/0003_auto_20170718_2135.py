# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20170717_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientsOfRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('count', models.IntegerField()),
                ('ingridient_id', models.ForeignKey(to='recipes.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
            ],
        ),
        migrations.RenameModel(
            old_name='Set_of_tag',
            new_name='SetOfTag',
        ),
        migrations.RemoveField(
            model_name='ingridients_of_recipe',
            name='ingridient_id',
        ),
        migrations.RemoveField(
            model_name='ingridients_of_recipe',
            name='measure_id',
        ),
        migrations.RemoveField(
            model_name='ingridients_of_recipe',
            name='recipe_id',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cuisine_id',
            new_name='cuisine',
        ),
        migrations.RenameField(
            model_name='step',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='measure',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.DeleteModel(
            name='Ingridient',
        ),
        migrations.DeleteModel(
            name='Ingridients_of_recipe',
        ),
        migrations.AddField(
            model_name='ingredientsofrecipe',
            name='measure_id',
            field=models.ForeignKey(to='recipes.Measure'),
        ),
        migrations.AddField(
            model_name='ingredientsofrecipe',
            name='recipe_id',
            field=models.ForeignKey(to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default=1, to='recipes.User'),
            preserve_default=False,
        ),
    ]
