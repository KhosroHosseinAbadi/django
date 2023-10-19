from django.urls import path
from . import views

app_name = "schools"

urlpatterns = [
    path("", views.SchoolListView.as_view(), name="list_school"),
    path("create/", views.SchoolCreateView.as_view(), name="create_school"),
    path("detail/<int:pk>/", views.SchoolDetailView.as_view(), name="detail_school"),
    path("update/<int:pk>/", views.SchoolUpdateView.as_view(), name="update_school"),
    path("delete/<int:pk>/", views.SchoolDeleteView.as_view(), name="delete_school"),
]
