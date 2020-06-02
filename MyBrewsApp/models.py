from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Brewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Fermentable(models.Model):
    name = models.CharField(max_length=200)
    pounds = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    lovibond = models.CharField(max_length=5, null=True, blank=True)
    # grain_type = models.CharField(max_length=2, choices=FERMENTABLE_TYPES, null=True, blank=True)
    brewer = models.ForeignKey(Brewer, on_delete=models.CASCADE, null=True, blank=True)
    ppg = models.IntegerField(default=0, null=True, blank=True)
    

    def __str__(self):
        return self.name

class Grist(models.Model):
    fermentable = models.ForeignKey(Fermentable, on_delete=models.CASCADE)
    pounds = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    brewer = models.ForeignKey(Brewer, on_delete=models.CASCADE, null=True, blank=True)


class Yeast(models.Model):
    name = models.CharField(max_length=200)
    brewer = models.ForeignKey(Brewer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Hop(models.Model):
    name = models.CharField(max_length=200)
    alpha_acid = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    # ounces = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    # boil_time = models.IntegerField(default=0)
    
    # dry_hopped = models.BooleanField(default=False)
    brewer = models.ForeignKey(Brewer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Water(models.Model):
    name = models.CharField(max_length=200, default='water', editable=False)
    brewer = models.ForeignKey(Brewer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    # ingredients
    name = models.CharField(max_length=200)
    grist = models.ForeignKey(Grist, on_delete=models.CASCADE, default=1)
    yeast = models.ForeignKey(Yeast, on_delete=models.CASCADE, default=1, null=True, blank=True)
    water = models.ForeignKey(Water, on_delete=models.CASCADE, null=True, blank=True)

    hop = models.ForeignKey(Hop, on_delete=models.CASCADE, null=True, blank=True)
    hop_ounces = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    hop_boil_time = models.IntegerField(default=0)

    batch_volume = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    boil_volume = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    brewer = models.ForeignKey(Brewer, on_delete=models.CASCADE, null=True, blank=True)

    # recipe stats
    target_og = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    original_gravity = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    final_gravity = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    abv = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ibu = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    brew_date = models.DateField(default=date.today, null=True, blank=True)
    srm = models.IntegerField(default=0, null=True, blank=True)
    utilization = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)

    # # water
    # batch_volume = models.DecimalField(max_digits=5, decimal_places=2)
    # boil_volume = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


