# Generated by Django 3.1.3 on 2021-02-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaxproApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOffered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(default='', max_length=50)),
                ('course_category', models.CharField(default='', max_length=50)),
                ('course_desc', models.TextField()),
                ('course_image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]
