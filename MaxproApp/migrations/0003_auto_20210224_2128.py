# Generated by Django 3.1.7 on 2021-02-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaxproApp', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
