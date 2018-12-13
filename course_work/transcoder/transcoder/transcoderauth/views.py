# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from helpers.django_request_helpers import django_get, django_get_or_post


# Create your views here.
@django_get
def logout(request):
    return render(request, 'index.html')


@django_get_or_post
def login(request):
    return render(request, 'login.html')


@django_get_or_post
def register(request):
    return render(request, 'register.html')
