from django.db import models
from django.core.validators import RegexValidator
# from accounts_app.models import User

# Create your models here.
class Contact(models.Model):
    
    email       =models.EmailField(max_length=55)
    name        =models.CharField(max_length=20)
    
    phone       =models.IntegerField()
    queries     =models.TextField()
    
    def __str__(self):
        return self.email
    