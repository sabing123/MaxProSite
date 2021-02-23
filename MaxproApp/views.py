from django.shortcuts import render

from .models import Aboutus


# Create your views here.

def index(request):
    return render(request, 'index.html')

def courseDetails(request):
    return render(request, 'course-detail.html')

def course(request):
    return render(request, 'course.html')



def aboutus(request):
    ab1 = Aboutus.objects.filter(about_category='MaxPro Computer')
    ab2 = Aboutus.objects.filter(about_category='About Us')
    ab3 = Aboutus.objects.filter(about_category='About Classes')
    params = {'ab1': ab1, 'ab2': ab2, 'ab3': ab3}
    return render(request, 'about.html', params)
