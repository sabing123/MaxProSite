from django.contrib import admin

from .models import Aboutus, Contact, CourseOffered, Gallery, PremiumCourses

# Register your models here.
admin.site.register(Aboutus)
admin.site.register(Contact)
admin.site.register(CourseOffered)
admin.site.register(Gallery)
admin.site.register(PremiumCourses)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'



