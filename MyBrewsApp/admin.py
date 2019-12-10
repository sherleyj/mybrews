from django.contrib import admin
from .models import Fermentable, Yeast, Hop, Brewer, Water, Recipe, Grist

# Register your models here.
admin.site.register(Fermentable)
admin.site.register(Yeast)
admin.site.register(Hop)
admin.site.register(Water)
admin.site.register(Recipe)
admin.site.register(Brewer)
admin.site.register(Grist)
