"""icallback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from icallback_base import urls as base_urls
from icallback_auth import urls as auth_urls
from icallback_app import urls as app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(auth_urls, namespace='icallback_auth')),
    path('account/', include(app_urls, namespace='icallback_app')),
    path('', include(base_urls, namespace='icallback_base'))
]
