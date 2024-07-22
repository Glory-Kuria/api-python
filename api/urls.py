
from django.urls import path
from .views import (
    StudentListView,
    ClassPeriodListView,
    CourseListView,
    TeacherListView,
    ClassroomListView,
    StudentDetailView,
    TeacherDetailView,
    CourseDetailView,
    ClassPeriodDetailView,
  
)

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student_list_view"),
    path("class-periods/", ClassPeriodListView.as_view(), name="classperiod-list-view"),  
    path("course/", CourseListView.as_view(), name="course-list-view"),
    path("teacher/", TeacherListView.as_view(), name="teacher-list-view"),
    path("classroom/", ClassroomListView.as_view(), name="classroom-list-view"),
    path("student/<int:id>/", StudentDetailView.as_view(), name="studentdetail_view"),
    path("teacher/<int:id>/", TeacherDetailView.as_view(), name="teacherdetail_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="coursedetail_view"),
    path("classperiod/<int:id>/", ClassPeriodDetailView.as_view(), name="classperioddetail_view"),
   
]
