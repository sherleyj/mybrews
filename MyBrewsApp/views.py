from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from MyBrewsApp.models import *
from MyBrewsApp.forms import *

# request.user.is_authenticated

def index(request):
    return render(request, 'MyBrewsApp/index.html')

def brewer(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    brewer = Brewer.objects.get(user=user)
    return render(request, 'MyBrewsApp/brewerHome.html', {'user': user, 'brewer': brewer})

@login_required
def brewerLoginRedirect(request):
    return HttpResponseRedirect(
        reverse('MyBrewsApp:brewer',args=[request.user.id])
    )


def addRecipe(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    brewer = Brewer.objects.get(user=user)
    
    if request.method == 'POST':
        recipe_fermentable_form = RecipeFermentableForm(request.POST)
        recipe_hop_form = RecipeHopForm(request.POST)
        recipe_yeast_form = RecipeYeastForm(request.POST)
        recipe_recipe_form = RecipeRecipeForm(request.POST)

        if recipe_fermentable_form.is_valid() and recipe_hop_form.is_valid() and recipe_yeast_form.is_valid() and recipe_recipe_form.is_valid():
            # try:
            fermentable_name = recipe_fermentable_form.cleaned_data['fermentable']
            pounds = recipe_fermentable_form.cleaned_data['pounds']
            yeast_name = recipe_yeast_form.cleaned_data['name']
            hop_name = recipe_hop_form.cleaned_data['hop']
            hop_ounces = recipe_hop_form.cleaned_data['hop_ounces']
            hop_boil_time = recipe_hop_form.cleaned_data['hop_boil_time']
            
            
            recipe_name = recipe_recipe_form.cleaned_data['name']
            batch_vol = recipe_recipe_form.cleaned_data['batch_volume']
            boil_vol = recipe_recipe_form.cleaned_data['boil_volume']
            brew_date = recipe_recipe_form.cleaned_data['brew_date']
            

            new_fermentable = Fermentable.objects.create(name=fermentable_name, brewer=brewer)
            new_grist = Grist.objects.create(fermentable=new_fermentable, pounds=pounds)
            new_hop = Hop.objects.create(name=hop_name)
            new_yeast = Yeast.objects.create(name=yeast_name)
            new_recipe = Recipe.objects.create(name=recipe_name, grist=new_grist, hop=new_hop, yeast=new_yeast, batch_volume=batch_vol, boil_volume=boil_vol, brew_date=brew_date,hop_ounces=hop_ounces, hop_boil_time = hop_boil_time)
            # except:
            #     recipe_fermentables_form = RecipeFermentableForm()
            #     return render(request, 'MyBrewsApp/addRecipe.html', {'user': user, 'brewer': brewer, 'RecipeFermentableForm': recipe_fermentable_form, 'error_message': 'Something went wrong.'})
            # do something.
    else:
        recipe_fermentable_form = RecipeFermentableForm()
        recipe_hop_form = RecipeHopForm()
        recipe_yeast_form = RecipeYeastForm()
        recipe_recipe_form = RecipeRecipeForm()
    return render(request, 'MyBrewsApp/addRecipe.html', {'user': user, 'brewer': brewer, 'RecipeFermentableForm': recipe_fermentable_form, 'RecipeHopForm': recipe_hop_form, 'RecipeYeastForm': recipe_yeast_form, 'RecipeRecipeForm':recipe_recipe_form})

