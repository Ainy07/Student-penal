from django.db import models
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=200)
    
    
class Course(models.Model):
    coursename = models.CharField(max_length=200)
    coursefees=models.IntegerField()
    courseduration=models.CharField(max_length=100)
    coursetextbox=models.TextField()    