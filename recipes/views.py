from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Recipe, Step
from .forms import RecipeForm, RegisterForm, UserForm, StepForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages

from django.contrib.auth.models import User



def recipes_list(request):
    recipes = Recipe.objects.all()
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
            recipe.update_time = timezone.now()
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_edit.html', {'form': form})


def step_new(request, pk_recipe):
    if request.method == "POST":
        print('0')
        print(pk_recipe)
        form = StepForm(request.POST)
        #form.fields.recipe = get_object_or_404(Recipe, pk=pk_recipe)
        if form.is_valid():

            step = form.save(commit=False)
            step.recipe = get_object_or_404(Recipe, pk=pk_recipe)
            step.save()
            return redirect('recipe_detail', pk=pk_recipe)
    else:
        form = StepForm()
        #form.fields.recipe = get_object_or_404(Recipe, pk=pk_recipe)

    return render(request, 'recipes/step_edit.html', {'form': form})


def step_edit(request, pk):
    step = get_object_or_404(Step, pk=pk)
    if request.method == "POST":
        form = StepForm(request.POST, instance=step)
        if form.is_valid():
            step = form.save(commit=False)
            step.save()
            return redirect('recipe_detail', pk=step.recipe.pk)
    else:
        form = StepForm(instance=step)
    return render(request, 'recipes/step_edit.html', {'form': form})


def step_delete(request, pk):
    step = get_object_or_404(Step, pk=pk)
    step.delete()
    return redirect('recipe_detail', pk=step.recipe.pk)


class RegisterFormView(FormView):
    template_name = "recipes/register.html"
    success_url = "/"
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)

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
            #user = form.save(commit=False)
            request.user.set_password(request.POST['password'])
            request.user.save()
            update_session_auth_hash(request, request.user)

            return render(request, 'recipes/author.html', {'form': form})

    else:
        form = UserForm(instance=user)

    return render(request, 'recipes/author.html', {'form': form})


