from django.db import models
from landing.models import customuser
User = customuser

# Create your models here.


class Documents(models.Model):
    file_name = models.CharField(max_length=150, null=True)
    docfile = models.FileField(upload_to='prototype')
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(customuser, on_delete=models.CASCADE, null=True)
    file_size = models.CharField(max_length=50, null=True)
    totalchunk = models.IntegerField(null=True)
