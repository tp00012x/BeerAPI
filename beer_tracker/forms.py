from django import forms
from django.contrib.auth.models import User
from beer_tracker.models import BeerModel, RateModel

# Create your forms here.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class NewBeerForm(forms.ModelForm):
    ibu = forms.IntegerField(label="IBU")
    abv = forms.IntegerField(label="ABV")
    locations = forms.CharField(label="Brewery Location")

    class Meta:
        model = BeerModel
        fields = ('user', 'name','ibu', 'calories', 'abv', 'style', 'location')

class RateForm(forms.ModelForm):

    class Meta:
        model = RateModel
        fields = ('beer', 'aroma','appearance', 'taste', 'overall')