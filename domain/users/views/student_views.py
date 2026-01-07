from django.views.generic import ListView
from domain.users.models.students import StudentProfile

class StudentListView(ListView):
    model = StudentProfile
    template_name = "students/student_list.html"