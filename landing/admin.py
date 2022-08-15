from django.contrib import admin
from .models import customuser
from .models import Contact

admin.site.register(Contact)
admin.site.register(customuser)

