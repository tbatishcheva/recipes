from django.contrib import admin
from .models import Recipe, Cuisine

admin.site.register(Recipe)
admin.site.register(Cuisine)