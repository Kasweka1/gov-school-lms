from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_number = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    job_title = models.CharField(max_length=100) 
