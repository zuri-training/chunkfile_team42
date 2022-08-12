import uuid
from django.db import models

# Create your models here.


class Document(models.Model):
    docfile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    docfile = models.FileField(upload_to='prototype')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(user)

