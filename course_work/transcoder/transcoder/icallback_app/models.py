import uuid

from django.contrib.auth.models import User
from django.db import models

from enum import Enum

# Create your models here.
from django.db.models import Manager

from helpers.model_helpers import list_enum


class Widget(models.Model):
    user = models.ForeignKey(User, related_name='widgets', on_delete=models.PROTECT, null=True, blank=True)

    site_name = models.CharField(max_length=140, blank=True)

    widget_key = models.CharField(max_length=140, blank=True, default=uuid.uuid1)
    active = models.BooleanField(default=False)

    objects = Manager()

    def __str__(self):
        return 'Widget [%s]' % self.site_name


class CallStatusType(Enum):
    OPERATOR_ANSWERED = "OPERATOR_ANSWERED"
    CLIENT_ANSWERED = "CLIENT_ANSWERED"
    NO_ANSWER = "NO_ANSWER"
    FAILED = "FAILED"


class Call(models.Model):
    callId = models.CharField(max_length=140, blank=True)

    user = models.ForeignKey(User, related_name='calls', on_delete=models.PROTECT, null=True, blank=True)
    widget = models.ForeignKey(Widget, related_name='calls', on_delete=models.PROTECT, null=True, blank=True)

    client_number = models.CharField(max_length=140, blank=True, null=True)
    operator_number = models.CharField(max_length=140, blank=True, null=True)

    status = models.CharField(max_length=140, choices=list_enum(CallStatusType), null=True)

    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_started = models.DateTimeField(default=None, null=True)
    time_answered = models.DateTimeField(default=None, null=True)
    time_ended = models.DateTimeField(default=None, null=True)
