# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def logout(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    return HttpResponse(status=405)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    return HttpResponse(status=405)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    return HttpResponse(status=405)
