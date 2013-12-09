from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Note(models.Model):
    
    username=models.OneToOneField(Student, primary_key=True)
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title

