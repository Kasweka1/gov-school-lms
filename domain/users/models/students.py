# domain/students/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date


class StudentProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    student_number = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    examination_number = models.CharField(max_length=50, null=True, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    # image = models.ImageField(upload_to='student_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.student_number}"
    
    def age(self):
        if not self.date_of_birth:
            return None
             
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None


class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    students = models.ManyToManyField(StudentProfile, related_name='parents')

