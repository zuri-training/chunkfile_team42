from django.db import models
from landing.models import customuser
User = customuser

# Create your models here.


class Documents(models.Model):
    file_name = models.CharField(max_length=150, null=True)
    docfile = models.FileField(upload_to='prototype')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_size = models.CharField(max_length=50, null=True)