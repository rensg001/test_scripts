from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=50)
    update_time = models.DateTimeField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)