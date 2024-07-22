from django.db import models

# Create your models here.
class ClassPeriod(models.Model):
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]

    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)

    def __str__(self):
        return f'{self.course} - {self.day_of_week} - {self.start_time}-{self.end_time}'