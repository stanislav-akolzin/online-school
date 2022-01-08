'''URLs of school app'''
from django.urls import path
from .import views


app_name = 'school'

urlpatterns = [
    path('courses/', views.TrainingCourseList.as_view()),
    path('my_courses/', views.MyCourses.as_view()),
    path('materials/', views.Materials.as_view()),
    path('grade/', views.Grade.as_view()),
]