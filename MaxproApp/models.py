from django.db import models

# Create your models here.

class Aboutus(models.Model):
    about_id = models.AutoField
    about_category = models.CharField(max_length=50, default="")
    about_desc = models.TextField()
    about_image = models.ImageField(upload_to="images/about", default="")

    def __str__(self):
        return self.about_category


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name + "-" +  self.email


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


