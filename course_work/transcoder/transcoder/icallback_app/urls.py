from django.urls import path

from icallback_app.views import settings, account, widget_delete, widget_toggle

app_name = 'icallback_app'

urlpatterns = [
    path('calls/', account, name='calls', kwargs={"active": "calls"}),
    path('widgets/', account, name='widgets', kwargs={"active": "widgets"}),
    path('statistics/', account, name='statistics', kwargs={"active": "statistics"}),
    path('settings/', settings, name='settings'),
    path('widget/delete/<int:widget_id>', widget_delete, name='widget_delete'),
    path('widget/toggle/<int:widget_id>', widget_toggle, name='widget_toggle'),
]
