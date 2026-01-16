from django.views.generic import ListView, DetailView
from domain.users.models.students import StudentProfile

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