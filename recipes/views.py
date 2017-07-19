from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Recipe, Step
from .forms import RecipeForm


def recipes_list(request):
    recipes = Recipe.objects.filter(creation_time__lte=timezone.now()).order_by('creation_time')
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})


def recipe_detail(request, pk):

    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.steps = recipe.step_set.all()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_edit.html', {'form': form})