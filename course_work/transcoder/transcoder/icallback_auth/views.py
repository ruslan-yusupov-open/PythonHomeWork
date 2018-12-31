# Create your views here.
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from helpers.django_request_helpers import django_get_or_post
from icallback_auth.forms import CustomCreationForm


@django_get_or_post
def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect(reverse('icallback_app:calls'))

        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': CustomCreationForm()})
