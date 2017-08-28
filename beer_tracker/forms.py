from django import forms
from django.contrib.auth.models import User
from beer_tracker.models import BeerModel

# Create your forms here.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class NewBeerForm(forms.ModelForm):
    class Meta:
        model = BeerModel
        fields = ('user', 'name','ibu', 'calories', 'abv', 'style', 'location')