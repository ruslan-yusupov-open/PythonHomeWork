from django.urls import path

from icallback_base.views import features, pricing, index, about

app_name = 'icallback_base'

urlpatterns = [
    path('features/', features, name='features'),
    path('pricing/', pricing, name='pricing'),
    path('about/', about, name='about'),
    path('', index, name='index'),
]
