from django.http import HttpResponse


def django_get(func):
    def get_func(request, *args, **kwargs):
        if request.method == 'GET':
            return func(request, *args, **kwargs)
        return HttpResponse(status=405)


def django_get_or_post(func):
    def get_func(request, *args, **kwargs):
        if request.method in ['GET', 'POST']:
            return func(request, *args, **kwargs)
        return HttpResponse(status=405)
