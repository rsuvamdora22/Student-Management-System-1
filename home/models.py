    
from django.db import models

class Gender(models.Model):
    gender = models.CharField(max_length=10)

class Student(models.Model):
    passphoto = models.ImageField(upload_to='passphotos/', blank=True, null=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    Email_id = models.EmailField()
    age = models.IntegerField()
    Date_of_birth = models.DateField(null=True)
    Address = models.TextField()
    Course = models.CharField(max_length=100)
    Year_of_passing = models.IntegerField()
    Percentage=models.IntegerField()
    gender = models.CharField(max_length=10,null=True)
    # gender = models.ForeignKey(Gender,on_delete=models.CASCADE)

class RemovedStudent(models.Model):
    passphoto = models.ImageField(upload_to='passphotos/', blank=True, null=True)
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    Email_id = models.EmailField()
    age = models.IntegerField()
    Date_of_birth = models.DateField(default='1947-01-01')
    Address = models.TextField()
    Course = models.CharField(max_length=255)
    Year_of_passing = models.IntegerField()
    Percentage=models.IntegerField()
    gender = models.CharField(max_length=10)


