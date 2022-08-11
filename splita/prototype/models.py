import uuid
import os
from django.db import models

# Create your models here.


class Document(models.Model):

    def __str__(self):
        return self.name

    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext

    docfile_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    docfile = models.FileField(upload_to='prototype')
    docfile_size = filesize
    #user = models.ForeignKey(user)
