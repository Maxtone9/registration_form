from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=10, choices=[('student', 'Student'), ('staff', 'Staff'), ('admin', 'Admin'), ('editor', 'Editor')])
    country = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
