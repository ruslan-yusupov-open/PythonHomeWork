from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from helpers.django_request_helpers import django_get, django_get_or_post
from icallback_app.forms import WidgetCreationForm
from icallback_app.models import Widget, Call


@login_required
@django_get_or_post
def account(request, active):
    widgets = Widget.objects.filter(user=request.user.id).all()
    calls = Call.objects.filter(user=request.user.id).all()

    if request.method == 'POST':
        widget_form = WidgetCreationForm(request.POST)
        if widget_form.is_valid():
            widget = widget_form.save(commit=False)
            widget.user = request.user
            widget.save()
            widget_form = WidgetCreationForm()
    else:
        widget_form = WidgetCreationForm()

    return render(request, 'account.html', {
        "active_tab": active,
        "widgets": widgets,
        "widget_form": widget_form,
        "calls": calls,
    })


@login_required
@django_get
def settings(request):
    return render(request, 'settings.html')


@login_required
@django_get
def widget_delete(request, widget_id):
    print("toggling", widget_id)
    widget_to_delete = Widget.objects.get(pk=widget_id)

    if widget_to_delete:
        widget_to_delete.delete()
    else:
        pass  # TODO: throw an error

    return redirect('icallback_app:widgets')


@login_required
@django_get
def widget_toggle(request, widget_id):
    widget_to_toggle = Widget.objects.get(pk=widget_id)

    if widget_to_toggle:
        widget_to_toggle.active = not widget_to_toggle.active
        widget_to_toggle.save()
    else:
        pass  # TODO: throw an error

    return redirect('icallback_app:widgets')
