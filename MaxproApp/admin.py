from django.contrib import admin
from .models import Aboutus, Contact

# Register your models here.
admin.site.register(Aboutus)
admin.site.register(Contact)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

