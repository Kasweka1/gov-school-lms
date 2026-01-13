from django.urls import path
from domain.users.views.student_views import StudentListView

app_name = 'user'
urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
]
