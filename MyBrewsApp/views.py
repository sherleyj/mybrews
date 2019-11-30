from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from MyBrewsApp.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# request.user.is_authenticated

def index(request):
    return render(request, 'MyBrewsApp/index.html')

def brewer(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    brewer = Brewer.objects.get(user=user)
    return render(request, 'MyBrewsApp/brewerHome.html', {user: user, brewer: brewer})

@login_required
def brewerLoginRedirect(request):
    return HttpResponseRedirect(
        reverse('MyBrewsApp:brewer',args=[request.user.id])
    )


def addRecipe(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    brewer = Brewer.objects.get(user=user)
    return render(request, 'MyBrewsApp/addRecipe.html', {user: user, brewer: brewer})

class MyLoginView():

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('account_landing', kwargs={'pk': self.request.user.pk, 'name': self.request.user.username})
