from django.db import models

# Create your models here.

class Klass(models.Model):
    name = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=128, null=False)


class Student(models.Model):
    name = models.CharField(max_length=20, null=False)
    birthday = models.DateField(null=False)
    gender = models.SmallIntegerField(null=False)
    klass = models.ForeignKey(Klass, related_name='students')