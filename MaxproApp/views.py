from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Aboutus,CourseOffered
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import mail_admins

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def courseDetails(request,myid):
    courseinfo = CourseOffered.objects.filter(id=myid)
    print(courseinfo)
    return render(request, 'course-detail.html', {'courseinfo': courseinfo[0]})

def courseEnroll(request,myid):
    courseinfo = CourseOffered.objects.filter(id=myid)
    print(courseinfo)
    return render(request, 'enroll.html', {'courseinfo': courseinfo[0]})


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
        course=Book.objects.none()
    else:
        bookstitle = Book.objects.filter(title__icontains=query)
        booksauthor = Book.objects.filter(author__icontains=query)
        bookscategories = Book.objects.filter(categories__icontains=query)
        course = bookstitle.union(booksauthor).union(bookscategories)
    
    if course.count()==0:
        message.error(request,"No search result found")
    params = {'course': course, 'query': query}
    return render(request, 'search.html', params)