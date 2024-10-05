from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=10)
    year = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"

class QuotaRequest(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')])

    def __str__(self):
        return f"{self.student} - {self.course} ({self.status})"