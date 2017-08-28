from django.shortcuts import render
from beer_tracker.forms import UserForm, NewBeerForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def home(request):
    users = User.objects.order_by('username')
    dict = {'records':users}
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