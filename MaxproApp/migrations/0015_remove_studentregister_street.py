# Generated by Django 3.1.7 on 2021-04-30 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MaxproApp', '0014_auto_20210430_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentregister',
            name='street',
        ),
    ]
