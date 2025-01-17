from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod
from course.models import Course
from teacher.models import Teacher
from classroom.models import ClassRoom



class StudentSerializers(serializers.ModelSerializer):
    class meta:
        model = Student
        fields = "__all__"

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'
        
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
               
        
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
        