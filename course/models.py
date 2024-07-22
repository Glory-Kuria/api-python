from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_trainer = models.CharField(max_length=100)
    course_objective = models.CharField(max_length=255)
    course_duration = models.DurationField()
    course_description = models.TextField()
    pass_mark = models.IntegerField()
    course_title = models.CharField(max_length=100)
    course_teacher = models.CharField(max_length=100)
    course_resources = models.CharField(max_length=255)
    teaching_assistant = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.course_name



# class Course(models.Model):
#     course_name =models.CharField(max_length = 20)
#     course_id = models.PositiveSmallIntegerField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     enrolment_capacity = models.PositiveSmallIntegerField()
#     department_id =models.IntegerField()
#     department = models.CharField(max_length=20)
#     Syllabus = models.TextField()
#     course_duration = models.IntegerField()
    
    
#     def __str__(self):
#           return f"{self.course_name} {self.course_code}"