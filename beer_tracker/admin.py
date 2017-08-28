from django.contrib import admin
from beer_tracker.models import BeerModel, RateModel

# Register your models here.
admin.site.register(BeerModel)
admin.site.register(RateModel)
