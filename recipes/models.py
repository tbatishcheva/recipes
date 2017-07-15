from django.db import models
from django.utils import timezone


class Cuisine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Ingridient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Measure(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=63)
    main_img = models.CharField(max_length=63)
    cuisine_id = models.ForeignKey(Cuisine)
    cooking_time = models.IntegerField()
    creation_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    # def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.name


class Step(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe_id = models.ForeignKey(Recipe)
    number = models.IntegerField()
    description = models.TextField()
    img = models.CharField(max_length=255)

    def __str__(self):
        return str(self.recipe_id) + ' ' + str(self.number) + ' step'


class Ingridients_of_recipe(models.Model):
    recipe_id = models.ForeignKey(Recipe)
    ingridient_id = models.ForeignKey(Ingridient)
    measure_id = models.ForeignKey(Measure)
    count = models.IntegerField()


class Set_of_tag(models.Model):
    recipe_id = models.ForeignKey(Recipe)
    tag_id = models.ForeignKey(Tag)
