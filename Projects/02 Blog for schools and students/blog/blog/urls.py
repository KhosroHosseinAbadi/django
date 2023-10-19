from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("schools/", include("schools.urls")),
    path("studunts/", include("students.urls")),
]
