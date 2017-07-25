from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Cuisine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Measure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    main_img = models.CharField(max_length=255)
    cuisine = models.ForeignKey(Cuisine)
    cooking_time = models.IntegerField()
    creation_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    # def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.name


class Step(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    number = models.IntegerField()
    description = models.TextField()
    img = models.CharField(max_length=255)

    def __str__(self):
        return str(self.recipe) + ' ' + str(self.number) + ' step'


class IngredientsOfRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipe)
    ingredient_id = models.ForeignKey(Ingredient)
    measure_id = models.ForeignKey(Measure)
    count = models.IntegerField()


class SetOfTag(models.Model):
    recipe_id = models.ForeignKey(Recipe)
    tag_id = models.ForeignKey(Tag)
