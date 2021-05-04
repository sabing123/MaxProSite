from django.contrib import admin
<<<<<<< HEAD
from .models import Aboutus, CourseOffered, Gallery, PremiumCourses, StudentRegister
=======

from .models import Aboutus, CourseOffered, Gallery, StudentRegister, PremiumCourses
>>>>>>> master

# Register your models here.
admin.site.register(Aboutus)
admin.site.register(CourseOffered)
admin.site.register(Gallery)
<<<<<<< HEAD
admin.site.register(PremiumCourses)
admin.site.register(StudentRegister)
=======

admin.site.register(PremiumCourses)

admin.site.register(StudentRegister)

>>>>>>> master

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'



