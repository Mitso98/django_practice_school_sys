from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses),
    path('courses/<course_name>', views.course),
]
