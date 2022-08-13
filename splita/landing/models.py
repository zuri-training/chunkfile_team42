from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators

class customuserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

   

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        user = self._create_user(email,
            password=password,  **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
      

class customuser(AbstractBaseUser, PermissionsMixin):
    username=None
    id = models.BigAutoField(primary_key = True,)
    email = models.EmailField(validators = [validators.EmailValidator()], unique=True, max_length = 200)
    fullname = models.CharField(max_length=50, blank=True)
    password = models.CharField( max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # profilepic = models.ImageField(null=True, blank=True, upload_to='image/')

    objects = customuserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'fullname']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Contact(models.Model):
    fullname = models.TextField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

