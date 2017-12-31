from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^services', views.services),
    url(r'^gallery', views.gallery),
    url(r'^contact', views.contact),
    url(r'^', views.index)
]
