from django.conf.urls import url
from beer_tracker import views

# TEMPLATE URLS!
app_name ='beer_tracker'

urlpatterns = [
    # url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name="user_login"),
]