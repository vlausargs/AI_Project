from django.db import models
from django.contrib.auth.models import User

class Recipes(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=500)
    steps = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=False,on_delete=models.CASCADE)

