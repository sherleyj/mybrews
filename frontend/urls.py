from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.index2, name='home2'),
    path('home/<int:user_id>/', views.index, name='home' ),
]