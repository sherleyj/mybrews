from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from MyBrewsApp.models import *
from MyBrewsApp.forms import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        brewer = Brewer.objects.get(id=user.id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# from django.contrib.sites.models import Site



# request.user.is_authenticated

# def index(request):
#         # return JsonResponse(data, safe=False)
#     return render(request, 'MyBrewsApp/index.html')

def brewer(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    brewer = Brewer.objects.get(user=user)
    return render(request, 'MyBrewsApp/brewerHome.html', {'user': user, 'brewer': brewer})
    # return render(request, 'frontend/index.html')


@login_required
def login_redirect(request):
    # return HttpResponseRedirect(
    #     reverse('MyBrewsApp:brewer',args=[request.user.id])
    # )
    return HttpResponseRedirect(
        reverse('frontend:home',args=[request.user.id])
    )

# def addRecipeForm(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     brewer = Brewer.objects.get(user=user)

    
#     if request.method == 'POST':
#         recipe_fermentable_form = RecipeFermentableForm(request.POST)
#         recipe_hop_form = RecipeHopForm(request.POST)
#         recipe_yeast_form = RecipeYeastForm(request.POST)
#         recipe_data_form = RecipeDataForm(request.POST)

#         if recipe_fermentable_form.is_valid() and recipe_hop_form.is_valid() and recipe_yeast_form.is_valid() and recipe_data_form.is_valid():
#             # try:
#             fermentable_name = recipe_fermentable_form.cleaned_data['fermentable']
#             pounds = recipe_fermentable_form.cleaned_data['pounds']
#             yeast_name = recipe_yeast_form.cleaned_data['name']
#             hop_name = recipe_hop_form.cleaned_data['hop']
#             hop_ounces = recipe_hop_form.cleaned_data['hop_ounces']
#             hop_boil_time = recipe_hop_form.cleaned_data['hop_boil_time']
            
            
#             recipe_name = recipe_data_form.cleaned_data['name']
#             batch_vol = recipe_data_form.cleaned_data['batch_volume']
#             boil_vol = recipe_data_form.cleaned_data['boil_volume']
#             brew_date = recipe_data_form.cleaned_data['brew_date']
            

#             new_fermentable = Fermentable.objects.create(name=fermentable_name, brewer=brewer)
#             new_grist = Grist.objects.create(fermentable=new_fermentable, pounds=pounds)
#             new_hop = Hop.objects.create(name=hop_name)
#             new_yeast = Yeast.objects.create(name=yeast_name)
#             new_recipe = Recipe.objects.create(name=recipe_name, grist=new_grist, hop=new_hop, yeast=new_yeast, batch_volume=batch_vol, boil_volume=boil_vol, brew_date=brew_date,hop_ounces=hop_ounces, hop_boil_time = hop_boil_time)
#             # except:
#             #     recipe_fermentables_form = RecipeFermentableForm()
#             #     return render(request, 'MyBrewsApp/addRecipe.html', {'user': user, 'brewer': brewer, 'RecipeFermentableForm': recipe_fermentable_form, 'error_message': 'Something went wrong.'})
#             # do something.
#     else:
#         recipe_fermentable_form = RecipeFermentableForm()
#         recipe_hop_form = RecipeHopForm()
#         recipe_yeast_form = RecipeYeastForm()
#         recipe_data_form = RecipeDataForm()
#     return render(request, 'MyBrewsApp/addRecipe.html', {'user': user, 'brewer': brewer, 'RecipeFermentableForm': recipe_fermentable_form, 'RecipeHopForm': recipe_hop_form, 'RecipeYeastForm': recipe_yeast_form, 'RecipeDataForm':recipe_data_form})

# def addRecipe(request, user_id):
#     data = {"test":123}
#     return JsonResponse(data, safe=False)

# def test(request):
#     data = {"test":123}
#     return JsonResponse(data, safe=False)

# def login(request):
#     un = request.POST['un']
#     psw = request.POST['psw']
    
#     if request.method == 'POST':
#         user = authenticate(username=un, password=psw)
#         failedResponse = {"response":"failed"}
#         if user is not None:
#             # return JsonResponse(failedResponse, safe=False)
#             serializer = UserSerializer
#         else:
#             return JsonResponse(failedResponse, safe=False)


class FermentableView(viewsets.ModelViewSet):
    # fermentables = Fermentable.objects.get(user=user)
    queryset = Fermentable.objects.all().order_by('name')
    serializer_class = FermentableSerializer

class UserView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class HopView(viewsets.ModelViewSet):
    queryset = Hop.objects.all()
    serializer_class = HopSerializer

class BrewerView(viewsets.ModelViewSet):
    queryset = Brewer.objects.all()
    serializer_class = BrewerSerializer

    