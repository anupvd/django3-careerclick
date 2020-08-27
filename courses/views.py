from django.shortcuts import render, get_object_or_404
from .models import Course

def courses(request):
    courses = Course.objects.order_by('-date')[:5]
    return render(request, 'courses/all_courses.html', {'courses': courses})

def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course.html', {'course': course})


