from django.contrib import admin

# Register your models here.
from icallback_app.models import Widget, Call

admin.site.register(Widget)
admin.site.register(Call)
