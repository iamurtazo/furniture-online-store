from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    image = models.ImageField(upload_to='users_images/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name   