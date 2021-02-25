from django.shortcuts import render
from .models import Aboutus
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import mail_admins

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