from django.db import models

# Create your models here.

class Aboutus(models.Model):
    about_id = models.AutoField
    about_category = models.CharField(max_length=50, default="")
    about_desc = models.TextField()
    about_image = models.ImageField(upload_to="images/about", default="")

    def __str__(self):
        return self.about_category
        


class CourseOffered(models.Model):
    course_id = models.AutoField
    course_title = models.CharField(max_length=50, default="")
    course_category = models.CharField(max_length=50, default="")
    course_desc = models.TextField()
    course_chapter = models.TextField()
    course_duration = models.CharField(max_length=50, default="")
    course_image = models.ImageField(upload_to="images/courses", default="")

    def __str__(self):
        return self.course_title

Gallery_CHOICES = (
    ('all','ALL'),
    ('lab', 'LAB'),
    ('classroom','CLASSROOM'),
    ('students','STUDENTS'),
    ('other','OTHER'),
)

class Gallery(models.Model):
    gallery_id = models.AutoField
    gallery_title = models.CharField(max_length=50, default="")
    gallery_cat = models.CharField(max_length=20, choices=Gallery_CHOICES, default='all')
    gallery_image = models.ImageField(upload_to="images/gallery", default="")

    def __str__(self):
        return self.gallery_title