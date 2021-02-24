from django.shortcuts import render

from .models import Aboutus, CourseOffered


# Create your views here.

def index(request):
    return render(request, 'index.html')

def courseDetails(request,myid):
    courseinfo = CourseOffered.objects.filter(id= myid)
    print(courseinfo)
    return render(request, 'course-detail.html', {'courseinfo': courseinfo[0]})

def course(request):
    courses = CourseOffered.objects.all()
    params = {'courses': courses}
    return render(request, 'course.html', params)



def aboutus(request):
    ab1 = Aboutus.objects.filter(about_category='MaxPro Computer')
    ab2 = Aboutus.objects.filter(about_category='About Us')
    ab3 = Aboutus.objects.filter(about_category='About Classes')
    params = {'ab1': ab1, 'ab2': ab2, 'ab3': ab3}
    return render(request, 'about.html', params)
