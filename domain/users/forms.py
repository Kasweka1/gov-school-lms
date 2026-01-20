from django import forms
from django.contrib.auth import get_user_model
from domain.users.models.students import StudentProfile

User = get_user_model()

class StudentCreateform(forms.Form):

    # User fields
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First name",
            "required":  True
        })
    )

    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last name",
            "required":  True
        })
    )

    
    middle_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Middle name (optional)"
        })
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email address"
        })
    )

    # Student fields
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date",
            "required":  True
        })
    )

    gender = forms.ChoiceField(
        choices=StudentProfile.GENDER_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select",
            "required":  True
        })
    )

    examination_number = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Examination number"
        })
    )

    enrollment_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date",
            "required":  True
        })
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
            "type": "file",
        })
    )