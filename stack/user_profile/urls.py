from django.conf.urls import url
from django.contrib import admin
from user_profile import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.LogOut.as_view(), name='logout'),
    url(r'^registration/$', views.Registration.as_view(), name='registr'),
]