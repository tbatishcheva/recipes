from django.shortcuts import render
from django.utils import timezone
from .models import Recipe


def recipes_list(request):
    recipes = Recipe.objects.filter(creation_time__lte=timezone.now()).order_by('creation_time')
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})
