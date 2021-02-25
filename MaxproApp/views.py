from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Aboutus, CourseOffered


def index(request):
    return render(request, 'index.html')


def courseDetails(request, myid):
    courseinfo = CourseOffered.objects.filter(id=myid)
    print(courseinfo)
    return render(request, 'course-detail.html', {'courseinfo': courseinfo[0]})


def course(request):
    courses = CourseOffered.objects.all()

    course_paginator = Paginator(courses, 1)
    page_num = request.GET.get('page')
    page = course_paginator.get_page(page_num)

    params = {'page': page}
    return render(request, 'course.html', params)


def aboutus(request):
    ab1 = Aboutus.objects.filter(about_category='MaxPro Computer')
    ab2 = Aboutus.objects.filter(about_category='About Us')
    ab3 = Aboutus.objects.filter(about_category='About Classes')
    params = {'ab1': ab1, 'ab2': ab2, 'ab3': ab3}
    return render(request, 'about.html', params)
