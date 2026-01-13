from django.views.generic import ListView
from domain.users.models.students import StudentProfile

class StudentListView(ListView):
    model = StudentProfile
    template_name = "domain/users/students/student_list.html"
    context_object_name = "students"

    