from django.conf.urls import url
from beer_tracker import views

# TEMPLATE URLS!
app_name ='beer_tracker'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^new_user/$', views.new_user, name="new_user"),
    url(r'^new_beer/$', views.new_beer, name="new_beer"),
    url(r'^rate_beer/$', views.rate_beer, name="rate_beer"),
]