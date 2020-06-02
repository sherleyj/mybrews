from django.shortcuts import render, get_object_or_404
from MyBrewsApp.models import *


def index(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    brewer = Brewer.objects.get(user=user)
    return render(request, 'frontend/index.html', {'user': user, 'brewer': brewer})

def index2(request):
    # return reverse('frontend:home2',args=(user.id))

    return render(request, 'frontend/index.html')

