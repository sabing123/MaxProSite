from django.contrib import admin
from .models import Aboutus, CourseOffered, Gallery, PremiumCourses, StudentRegister

# Register your models here.
admin.site.register(Aboutus)
admin.site.register(CourseOffered)
admin.site.register(Gallery)
admin.site.register(PremiumCourses)
admin.site.register(StudentRegister)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'



