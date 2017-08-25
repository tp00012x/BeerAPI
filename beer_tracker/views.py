from django.shortcuts import render
from beer_tracker.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'beer_tracker/home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def index(request):

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            return render(request, 'beer_tracker/home.html')
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'beer_tracker/index.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'beer_tracker/index.html')
    else:
        return render(request, "beer_tracker/index.html", {})

def new_user(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'beer_tracker/home.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})