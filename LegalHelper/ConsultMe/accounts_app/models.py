from django.db import models

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

from django.utils.translation import gettext_lazy as gtl
from django.contrib.auth.models import PermissionsMixin


# from core_app.models import Contact

# Create your models here.

class UserManager(BaseUserManager):
    """
    Custom User model manager where email is the unique identifiers
    for authentication instead of username
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a Superuser with the giver email and password
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(gtl("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(gtl("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    email           =models.EmailField(gtl("email address main"), unique=True)
    username        =models.CharField(gtl("Username"),max_length=55, blank=True)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    date_joined     =models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email
    
    #if not the code below then taking default value in User Model Not in proxy Model
    


class Lawyer(models.Model):
    user            = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email           = models.EmailField(gtl("email address main"), unique=True, default="")
    phone_number    = models.CharField(max_length=20,default="")
    address         = models.TextField(max_length=550,default="")
    expertise       = models.CharField(max_length=200,default="")
    created_at      = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email

class Client(models.Model):
    user            = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email           = models.EmailField(gtl("email address main"), unique=True, default="")
    username        = models.CharField(max_length=150, unique=True, default="")
    phone_number    = models.CharField(max_length=20,default="")
    address         = models.TextField(max_length=550,default="")
    created_at      = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email
    
class Communication(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.client.user.email} to {self.lawyer.user.email} - {self.timestamp}"


