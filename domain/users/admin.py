from django.contrib import admin
from domain.users.models.students import StudentProfile, ParentProfile
# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(ParentProfile)