from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("create/", views.StudentCreateView.as_view(), name="create_student"),
    path("update/<int:pk>/", views.StudentUpdateView.as_view(), name="update_student"),
    path("delete/<int:pk>/", views.StudentDeleteView.as_view(), name="delete_student"),
    path("add/<int:pk>/", views.add_student_to_school, name="add_student"),
]
