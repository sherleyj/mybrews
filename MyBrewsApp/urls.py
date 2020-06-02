from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'loginViewSet', views.loginViewSet)
router.register(r'fermentables', views.FermentableView)
router.register(r'users', views.UserView)
router.register(r'brewers', views.BrewerView)
router.register(r'hops', views.HopView)

app_name = 'api'
urlpatterns = [
    # # path('<int:user_id>/', views.brewerHome, name='brewerHome'),
    # path('', views.index, name='index'),
    path('loginredirect/', views.login_redirect, name='login_redirect'),
    path('brewer/<int:user_id>/', views.brewer, name='brewer'),
    # path('addrecipe/<int:user_id>/', views.addRecipeForm, name='addRecipe'),
    # path('addrecipe/<int:user_id>/', views.addRecipeForm, name='addRecipe'),
    # path('test/', views.test),
    # # path('login/', views.login),
    # path('myfermentables/<int:user_id>/', views.myFermetables),
    path('', include(router.urls)),
]