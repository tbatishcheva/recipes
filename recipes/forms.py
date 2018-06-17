from django import forms
from .models import Recipe, User, Step
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name',
                  'description',
                  'main_img',
                  'cuisine',
                  'cooking_time')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username",
                  "email")

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass


class UserForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  )


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = (
                  'description',
                  'number',
                  'img')