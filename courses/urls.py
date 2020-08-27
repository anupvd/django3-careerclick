from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.courses, name='all_courses'),
    path('<int:course_id>/', views.course, name = 'course'),
]