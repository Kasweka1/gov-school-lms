from django.views.generic import ListView, DetailView, FormView
from domain.users.forms import StudentCreateform
from domain.users.models.students import StudentProfile
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from domain.users.utils import generate_student_number, generate_student_password, generate_student_username
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

User = get_user_model()
class StudentListView(ListView):
    model = StudentProfile
    template_name = "domain/users/students/student_list.html"
    context_object_name = "students"

    
class StudentDetailView(DetailView):
    model = StudentProfile
    template_name = "domain/users/students/student_detail.html"
    context_object_name = "student"
    slug_field = "student_number"
    slug_url_kwarg = "student_number"


class StudentCreateView(FormView):
    model = StudentProfile
    template_name = "domain/users/students/student_form.html"
    form_class = StudentCreateform
    success_url = reverse_lazy("user:student_list")
    permission_required = 'users.add_studentprofile'

    def form_valid(self, form):
        student_number = generate_student_number()
        password = generate_student_password(form.cleaned_data["first_name"], form.cleaned_data["last_name"])
        
        # Create User instance
        user = User.objects.create_user(
            username=generate_student_username(form.cleaned_data["first_name"], form.cleaned_data["last_name"]),
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            email=form.cleaned_data["email"],
            password=password,
        )
        # Create StudentProfile instance
        StudentProfile.objects.create(
            user=user,
            middle_name=form.cleaned_data["middle_name"],
            gender=form.cleaned_data["gender"],
            student_number=student_number,
            date_of_birth=form.cleaned_data["date_of_birth"],
            examination_number=form.cleaned_data["examination_number"],
            enrollment_date=form.cleaned_data["enrollment_date"],
        )
        return super().form_valid(form)