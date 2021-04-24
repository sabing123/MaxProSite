from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Aboutus,CourseOffered
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import mail_admins

def index(request):
    return render(request, 'index.html')

def terms(request):
    return render(request, 'termsAndConditions.html')

def courseDetails(request,myid):
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

def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('contact')
    else:
        f = ContactForm()
    return render(request, 'contact.html', {'form': f})

def search(request):
    query = request.GET['query']
    if len(query)>78:
        course=CourseOffered.objects.none()
    else:
        coursetitle = CourseOffered.objects.filter(course_title__icontains=query)
        coursecategories = CourseOffered.objects.filter(course_category__icontains=query)
        course = coursetitle.union(coursecategories)
        page = request.GET.get('page', 1)
        paginator = Paginator(course, 2)
        try:
            course = paginator.page(page)
        except PageNotAnInteger:
            course = paginator.page(1)
        except EmptyPage:
            course = paginator.page(paginator.num_pages)
    params = {'course': course, 'query': query}
    return render(request, 'search.html', params)



