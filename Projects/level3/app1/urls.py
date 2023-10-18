from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_form_view, name='comment_form_view'),
]