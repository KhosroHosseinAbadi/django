# blog URL Configuration

from django.contrib import admin
from django.urls import path, include
from django.contrib import auth
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("posts/", include("posts.urls")),
    path("accounts/login/", auth.views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth.views.LogoutView.as_view(), name="logout", kwargs={"next_page": '/'}),
]
