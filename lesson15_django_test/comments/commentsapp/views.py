from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def comments(request):
    if request.method == 'GET':
        # comments = Comments.objects.all()
        return render(request, 'index.html')
    return HttpResponse(status=405)
