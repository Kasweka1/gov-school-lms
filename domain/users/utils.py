from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Max
from domain.users.models.students import StudentProfile

# Utility function to generate unique usernames for students

def generate_student_username(first_name: str, last_name: str) -> str:
    base = f"{first_name.lower()}-{last_name.lower()}"
    username = base
    counter = 1

    while User.objects.filter(username=username).exists():
        username = f"{base}-{counter}"
        counter += 1

    return username

# Utility function to generate default passwords for students

def generate_student_password(first_name: str, last_name: str) -> str:
    year = timezone.now().year
    password = f"{first_name.capitalize()}{last_name.capitalize()}@{year}"
    return password

# Utility function to generate unique student numbers

def generate_student_number() -> str:
    year = timezone.now().year
    prefix = f"STU-{year}-"

    # Get latest student number for this year
    latest = (
        StudentProfile.objects
        .filter(student_number__startswith=prefix)
        .aggregate(Max("student_number"))
        .get("student_number__max")
    )

    if latest:
        last_number = int(latest.split("-")[-1])
        next_number = last_number + 1
    else:
        next_number = 1

    return f"{prefix}{next_number:05d}"