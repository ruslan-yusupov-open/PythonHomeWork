from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    return HttpResponse(status=405)


def features(request):
    if request.method == 'GET':
        return render(request, 'features.html')
    return HttpResponse(status=405)


def pricing(request):
    if request.method == 'GET':
        return render(request, 'pricing.html')
    return HttpResponse(status=405)
