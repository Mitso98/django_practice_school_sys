from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students),
    path('students/<name>', views.student_name),
    
]
