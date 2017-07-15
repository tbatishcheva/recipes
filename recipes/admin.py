from django.contrib import admin
from .models import Recipe, Cuisine, Ingridient, Step, Ingridients_of_recipe, Set_of_tag, Measure, Tag

admin.site.register(Recipe)
admin.site.register(Cuisine)
admin.site.register(Ingridient)
admin.site.register(Step)
admin.site.register(Ingridients_of_recipe)
admin.site.register(Set_of_tag)
admin.site.register(Measure)
admin.site.register(Tag)