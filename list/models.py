from django.db import models

# Create your models here.

class Todo(models.Model):
    datet = models.DateField()
    text = models.CharField(max_length=200)
