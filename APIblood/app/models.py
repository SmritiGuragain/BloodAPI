from django.db import models
from datetime import date

# Create your models here.
class doner(models.Model):
    Fname=models.CharField(max_length=30)
    Lname=models.CharField(max_length=30)
    Age=models.IntegerField()
    Categorychoices=[
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
    ]
    Bloodgroup=models.CharField(choices=Categorychoices,max_length=20)
    def  __str__(self):
        return self.Fname
    
    '''def availability(self):
        hello=(date.today()-self.Date).days
        if(hello>=90):
            return "Available"
        else:
            return "Not Available"'''