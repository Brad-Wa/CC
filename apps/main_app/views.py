# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')
def contact(request):
    return render(request, 'main_app/contact.html')
def gallery(request):
    return render(request, 'main_app/gallery.html')
def services(request):
    return render(request, 'main_app/services.html')
