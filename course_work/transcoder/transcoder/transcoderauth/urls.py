from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path
from django.views.generic import CreateView

from transcoderauth.forms import CustomCreationForm, CustomLoginForm

app_name = 'transcoderauth'

urlpatterns = [

    path('login/', LoginView.as_view(
        template_name='login.html',
        form_class=CustomLoginForm
    ), name='login'),

    path('logout/', logout_then_login, name='logout'),

    path('register/', CreateView.as_view(
        template_name='register.html',
        form_class=CustomCreationForm,
        success_url='/',
    ), name='register'),
]
