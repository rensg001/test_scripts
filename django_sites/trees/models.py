from django.db import models

# Create your models here.


class TreeNode(models.Model):

    key = models.CharField(null=False, default='', max_length=10, unique=True)
    parent_key = models.CharField(null=True, blank=True, max_length=10)
    is_leaf = models.BooleanField(null=False)
    name = models.CharField(max_length=20)
