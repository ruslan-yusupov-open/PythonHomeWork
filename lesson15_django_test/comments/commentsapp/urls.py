from django.conf.urls import url

from commentsapp.views import comments

app_name = 'commentsapp'

urlpatterns = [
    url(r'', comments),
]
