from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# ------------------------
# USER MODEL
# -----------------------
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=255, blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    
    def __str__(self):
        return self.username