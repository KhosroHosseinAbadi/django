from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('school/create/', views.SchoolCreateView.as_view(), name='school_create'),
    path('', views.SchoolListView.as_view(), name='school_list'),
    path('school-<int:pk>/detail/', views.SchoolDetailView.as_view(), name='school_detail'),
    path('school-<int:pk>/update/', views.SchoolUpdateView.as_view(), name='school_update'),
    path('school-<int:pk>/delete/', views.SchoolDeleteView.as_view(), name='school_delete'),
    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student-<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student-<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('add-student-to-school-<int:pk>/', views.add_student_to_school, name='add_student_to_school'),
]