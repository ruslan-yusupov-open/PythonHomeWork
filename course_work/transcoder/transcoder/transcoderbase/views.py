from django.http import HttpResponse
from django.shortcuts import render

from helpers.django_request_helpers import django_get


# Create your views here.

@django_get
def index(request):
    return render(request, 'index.html')


@django_get
def features(request):
    return render(request, 'features.html')


@django_get
def pricing(request):
    return render(request, 'pricing.html')


@django_get
def about(request):
    return render(request, 'about.html')
