from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path
from django.views.generic import CreateView

from icallback_auth.forms import CustomCreationForm, CustomLoginForm

app_name = 'icallback_auth'

urlpatterns = [

    path('login/', LoginView.as_view(
        template_name='login.html',
        form_class=CustomLoginForm,
        success_url='/',
    ), name='login'),

    path('logout/', logout_then_login, name='logout'),

    path('register/', CreateView.as_view(
        template_name='register.html',
        form_class=CustomCreationForm,
        success_url='/',
    ), name='register'),
]
