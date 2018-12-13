
from django.utils import timezone

from django.db import models

# Create your models here.
from django.db.models import Manager


class Video(models.Model):
    rel_name = 'videos'
    # Linking:
    kind = models.ForeignKey('User', related_name='videos', on_delete=models.PROTECT)

    filename = models.CharField(max_length=140, blank=True)
    encoded = models.BooleanField(default=False)

    # Utils:
    date_created = models.DateTimeField(auto_now_add=True)
    date_encoded = models.DateTimeField(default=None, null=True)

    objects = Manager()

    def mark_encoded(self, commit=True):
        self.encoded = True
        self.date_encoded = timezone.now()
        if commit:
            self.save()

    def __str__(self):
        return 'Video [%s]' % self.filename
