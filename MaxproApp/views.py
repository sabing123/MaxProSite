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
<<<<<<< Updated upstream
=======

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

>>>>>>> Stashed changes
