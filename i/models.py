from django.db import models
# Create your models here.
class Student(models.Model):
    student_roll_number = models.CharField(max_length=50)
    student_full_name = models.CharField(max_length=50)
    student_mobile_no= models.CharField(max_length=50)
