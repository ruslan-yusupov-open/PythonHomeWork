from django.urls import path

from transcoderbase.views import features, pricing, index

app_name = 'transcoderbase'

urlpatterns = [
    path('features/', features, name='features'),
    path('pricing/', pricing, name='pricing'),
    path('about/', pricing, name='about'),
    path('', index, name='index'),
]
