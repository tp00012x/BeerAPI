from django import forms
from django.contrib.auth.models import User
from .models import BeerModel, RateModel

# Forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class NewBeerForm(forms.ModelForm):
    ibu = forms.IntegerField(label="IBU")
    abv = forms.IntegerField(label="ABV")
    location = forms.CharField(label="Brewery Location")

    class Meta:
        model = BeerModel
        fields = '__all__'

class RateForm(forms.ModelForm):

    class Meta:
        model = RateModel
        fields = '__all__'