from django.urls import path

from transcoderbase.views import features, pricing, index, about

app_name = 'transcoderbase'

urlpatterns = [
    path('features/', features, name='features'),
    path('pricing/', pricing, name='pricing'),
    path('about/', about, name='about'),
    path('', index, name='index'),
]
