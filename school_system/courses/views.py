from django.shortcuts import render

# Create your views here.


def courses(request):
    courses = ['C', 'C++', 'Java', 'JavaScript', 'Python']
    ctx = {
        'courses_list': courses
    }
    return render(request, 'courses_index.html', ctx)


def course(request, course_name):
    ctx = {
        'course_name': course_name
    }
    return render(request, 'course_info.html', ctx)
