from django.contrib import admin
<<<<<<< HEAD

from .models import Aboutus, Contact, CourseOffered, Gallery, PremiumCourses
=======
from .models import Aboutus, CourseOffered, Gallery, StudentRegister
>>>>>>> Rupesh-Branch

# Register your models here.
admin.site.register(Aboutus)
admin.site.register(Contact)
admin.site.register(CourseOffered)
admin.site.register(Gallery)
<<<<<<< HEAD
admin.site.register(PremiumCourses)
=======
admin.site.register(StudentRegister)
>>>>>>> Rupesh-Branch

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'



