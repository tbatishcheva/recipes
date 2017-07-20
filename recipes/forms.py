from django import forms
from .models import Recipe
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name',
                  'id',
                  'author',
                  'description',
                  'main_img',
                  'cuisine',
                  'cooking_time')


class ContactForm(forms.Form, UserCreationForm):
    email = forms.EmailField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass