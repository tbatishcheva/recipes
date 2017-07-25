from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Recipe
from .forms import RecipeForm, RegisterForm, UserForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.models import User


def recipes_list(request):
    recipes = Recipe.objects.filter(creation_time__lte=timezone.now()).order_by('creation_time')
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.creation_time = timezone.now()
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_edit.html', {'form': form})


def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            # recipe.author = request.user
            recipe.creation_time = timezone.now()
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_edit.html', {'form': form})


class RegisterFormView(FormView):
    success_url = "/"
    template_name = "recipes/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "recipes/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def author(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            return redirect('/', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'recipes/author.html', {'form': form})

