from django.db import models

# Create your models here.
class Teacher(models.Model):
    teachers_id=models.IntegerField()
    first_name= models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email=models.EmailField()
    phone_number = models.CharField(max_length=50)
    subject_specialization=models.CharField(max_length=20)
    years_of_experience=models.IntegerField()
    office_hours= models.CharField(max_length=20)
    biography= models.TextField()
    course_taught=models.CharField(max_length=50)
    hire_date =models.DateField()
    department = models.CharField(max_length=20)
    salary = models.FloatField()
    address = models.CharField(max_length=30)
    profile_picture = models.ImageField()
    
    def __str__(self):
     return f"{self.first_name}{self.last_name}"