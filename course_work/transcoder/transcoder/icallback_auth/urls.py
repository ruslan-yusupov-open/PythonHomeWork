from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path

from icallback_auth.forms import CustomLoginForm
from icallback_auth.views import register

app_name = 'icallback_auth'

urlpatterns = [

    path('login/', LoginView.as_view(
        template_name='login.html',
        form_class=CustomLoginForm,
        success_url='/',
    ), name='login'),

    path('logout/', logout_then_login, name='logout'),

    path('register/', register, name='register')

    # path('register/', CreateView.as_view(
    #     template_name='register.html',
    #     form_class=CustomCreationForm,
    #     success_url='/',
    # ), name='register'),
]
