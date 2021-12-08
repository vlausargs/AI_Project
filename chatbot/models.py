from django.db import models

# Create your models here.
class Tags(models.Model):
    tag = models.TextField(unique=True)

class Patterns(models.Model):
    pattern = models.TextField()
    tag = models.ForeignKey(Tags, blank=False,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tag', 'pattern',)

class Responses(models.Model):
    response = models.TextField()
    tag = models.ForeignKey(Tags, blank=False,on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('tag', 'response',)

