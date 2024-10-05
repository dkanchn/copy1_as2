from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from adminQuota.models import Course, QuotaRequest  # import โมเดล Course และ QuotaRequest

def index(request):
    students = Student.objects.all()
    return render(request, "students/index.html", {
        "students": students
    })

def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    quota_requests = QuotaRequest.objects.filter(student=student)
    return render(request, "students/student_detail.html", {
        "student": student,
        "quota_requests": quota_requests,
    })

def request_quota(request):
    if request.method == "POST":
        student = Student.objects.get(pk=int(request.POST["student"]))
        course = Course.objects.get(pk=int(request.POST["course"]))
        # สร้าง QuotaRequest ใหม่
        QuotaRequest.objects.create(student=student, course=course, status='pending')
        return redirect("students:student_detail", student_id=student.id)

    courses = Course.objects.all()
    students = Student.objects.all()
    return render(request, "students/request_quota.html", {
        "courses": courses,
        "students": students,
    })

def quota_status(request):
    quota_requests = QuotaRequest.objects.all()
    return render(request, "students/quota_status.html", {
        "quota_requests": quota_requests,
    })