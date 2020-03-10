from MyBrewsApp.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class FermentableSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="MyBrewsApp:fermentable-detail")
    brewer = serializers.HyperlinkedIdentityField(view_name="MyBrewsApp:brewer-detail")

    class Meta:
        model = Fermentable
        fields = ('id','url','name', 'lovibond', 'ppg', 'brewer')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="MyBrewsApp:user-detail")

    class Meta:
        model = User
        fields = ('id','url','username','first_name', 'last_name', 'email')

class HopSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="MyBrewsApp:hop-detail")

    class Meta:
        model = Hop
        fields = ('id','url','name','alpha_acid',)

class BrewerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="MyBrewsApp:brewer-detail")
    user = serializers.HyperlinkedIdentityField(view_name="MyBrewsApp:user-detail")

    class Meta:
        model = Brewer
        fields = ('id','url','user')