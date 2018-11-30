from django.db import models


# Create your models here.

class Post(models.Model):
    header = models.CharField(max_length=140, null=False)
    message = models.TextField(max_length=3000, null=False)

    def __str__(self):
        return str(self.header) + ": " + str(self.message)


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='posts', on_delete=models.PROTECT)

    message = models.TextField(max_length=3000, null=False)

    def __str__(self):
        return str(self.message)
