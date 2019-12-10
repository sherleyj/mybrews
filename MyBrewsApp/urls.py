from django.urls import path

from . import views

app_name = 'MyBrewsApp'
urlpatterns = [
    # path('<int:user_id>/', views.brewerHome, name='brewerHome'),
    path('', views.index, name='index'),
    path('brewerLoginRedirect/', views.brewerLoginRedirect, name='brewerLoginRedirect'),
    path('brewer/<int:user_id>/', views.brewer, name='brewer'),
    path('AddRecipe/<int:user_id>/', views.addRecipe, name='addRecipe')
]