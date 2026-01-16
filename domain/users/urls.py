from django.urls import path
from domain.users.views.student_views import StudentDetailView, StudentListView

app_name = 'user'
urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<str:student_number>/', StudentDetailView.as_view(), name='student_detail'),
]
