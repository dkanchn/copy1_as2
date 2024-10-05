from django.db import models

# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=10, null=False, blank=False)
    course_name = models.CharField(max_length=100, null=False, blank=False)
    semester = models.IntegerField()
    year = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.course_code}: {self.course_name} ({self.semester}/{self.year})"

    
class Enroll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name="enrollments")
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, through=Enroll, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"