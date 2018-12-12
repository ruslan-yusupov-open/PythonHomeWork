from django.urls import path

from transcoderauth.views import login, register, logout

app_name = 'transcoderauth'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout')
]
