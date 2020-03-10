from MyBrewsApp.models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime

# class RecipeFermentableForm(ModelForm):
#     class Meta:
#         model = Fermentable
#         fields = ['name']

# class RecipeGristForm(ModelForm):
#     class Meta:
#         model = Grist
#         fields = ['pounds']
    
# each item in Grist
class RecipeFermentableForm(forms.Form):
    fermentable = forms.CharField(max_length=200)
    pounds = forms.DecimalField(max_digits=3, decimal_places=1)
    

class RecipeHopForm(forms.Form):
    hop = forms.CharField(max_length=200)
    hop_boil_time = forms.DecimalField(max_digits=3, decimal_places=1)
    hop_ounces = forms.IntegerField()

class RecipeYeastForm(ModelForm):
    class Meta:
        model = Yeast
        fields = ['name']
        labels = {'name': 'Yeast'}

class RecipeDataForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','brew_date','batch_volume', 'boil_volume']
        labels = {'name': 'Recipe name'}

# Fermentable will have to change to a list of fermentables?
class RecipeForm(forms.Form):
    name = forms.CharField(max_length=200)
    brew_date = forms.DateField(initial=datetime.date.today)
    fermentable = forms.CharField(max_length=200)
    pounds = forms.DecimalField(max_digits=3, decimal_places=1)
    hop = forms.CharField(max_length=200)
    hop_boil_time = forms.DecimalField(max_digits=3, decimal_places=1)
    hop_ounces = forms.IntegerField()
    yeast = forms.CharField(max_length=200)
    batch_volume = models.DecimalField(max_digits=5, decimal_places=2)
    boil_volume = models.DecimalField(max_digits=5, decimal_places=2)
    labels = {'name': 'Recipe name', 'name': 'Yeast'}
