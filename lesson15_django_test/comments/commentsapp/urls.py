from django.conf.urls import url

from commentsapp.views import comments
app_name = 'pizza_app'

urlpatterns = [
    url(r'', comments, name='comments'),
]
