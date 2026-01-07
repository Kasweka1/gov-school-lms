from django.urls import path
from domain.users.views.student_views import StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='dashboard'),
]
