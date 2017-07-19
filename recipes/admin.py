from django.contrib import admin
from .models import Recipe, Cuisine, Ingredient, Step, IngredientsOfRecipe, SetOfTag, Measure, Tag, User

admin.site.register(Recipe)
admin.site.register(Cuisine)
admin.site.register(Ingredient)
admin.site.register(Step)
admin.site.register(IngredientsOfRecipe)
admin.site.register(SetOfTag)
admin.site.register(Measure)
admin.site.register(Tag)
admin.site.register(User)
