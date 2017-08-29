from django.contrib import admin
from .models import BeerModel, RateModel

admin.site.register(BeerModel)
admin.site.register(RateModel)