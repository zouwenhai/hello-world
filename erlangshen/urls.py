from django.conf.urls import url
from django.conf.urls import include

from . import views


urlpatterns = [
    url(r'^signup/$', views.Signup()),
    url(r'^login/$', views.Login()),
    url(r'^logout/$', views.Logout()),
    url(r'^account/$', views.AccountView()),
]
