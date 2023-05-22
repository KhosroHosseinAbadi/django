from django.urls import path
from . import views

app_name = 'application1'

urlpatterns = [
    path('index/', views.app1_index, name='index'),
    path('index/page1/', views.app1_page1, name='page1'),
    path('index/page2/', views.app1_page2, name='page2'),

]