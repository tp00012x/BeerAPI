from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserForm, NewBeerForm, RateForm
from .models import BeerModel

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BeerModelSerializer

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def home(request):
    beers = BeerModel.objects.order_by('name')
    dict = {'records':beers}
    return render(request, 'beer_tracker/home.html', context=dict)

@login_required
def new_user(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('beer_tracker:home'))
    else:
        user_form = UserForm()

    return render(request, 'beer_tracker/new_user.html', {'user_form':user_form})

@login_required
def new_beer(request):
    if request.method == "POST":
        beer = NewBeerForm(request.POST)
        if beer.is_valid():
            beer.save(commit=True)
            return HttpResponseRedirect(reverse('beer_tracker:home'))
    else:
        beer = NewBeerForm()

    return render(request, 'beer_tracker/new_beer.html', {'beer':beer})

@login_required
def rate_beer(request):
    if request.method == "POST":
        rate_beer = RateForm(request.POST)
        if rate_beer.is_valid():
            rate_beer.save(commit=True)
            return HttpResponseRedirect(reverse('beer_tracker:home'))
    else:
        rate_beer = RateForm()

    return render(request, 'beer_tracker/rate_beer.html', {'rate_beer':rate_beer})

def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('beer_tracker:home'))
    else:
        user_form = UserForm()

    return render(request, 'beer_tracker/index.html', {'user_form': user_form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('beer_tracker:home'))
        else:
            user_form = UserForm()
            return render(request, 'beer_tracker/index.html', {'invalid':True,'user_form': user_form})

# Show list of beers as JSON
class BeerModelList(APIView):
    def get(self, request):
        beers = BeerModel.objects.all()
        serializer = BeerModelSerializer(beers, many=True)
        return Response(serializer.data)