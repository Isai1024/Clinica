from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class User(models.Model):
    
    class TypeUser(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        DOCTOR = 'DOCTOR', 'Doctor'
        PATIENT = 'PATIENT', 'Patient'
    
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    email = models.EmailField(max_length=254, unique=True)
    encrypted_password = models.CharField(max_length=128)
    salt = models.CharField(max_length=64)
    
    typeUser = models.CharField(
        max_length=10,
        choices=TypeUser.choices,
        default=TypeUser.PATIENT,
    )
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        db_table = 'users'
        ordering = ['user_id']