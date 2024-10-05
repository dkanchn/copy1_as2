from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Course, QuotaRequest
from students.models import Student  # โมเดล Student คาดว่ามาจากแอป students

def index(request):
    courses = Course.objects.all()
    return render(request, "courses/index.html", {
        "courses": courses
    })

def course(request, course_id):
    course = Course.objects.get(pk=course_id)
    # แสดงนักเรียนที่ยังไม่ได้ทำการขอโควต้าสำหรับคอร์สนี้
    nonstudents = Student.objects.exclude(quota_request__course=course).all()
    return render(request, "courses/course.html", {
        "course": course,
        "nonstudents": nonstudents,
    })

def request_quota(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == "POST":
        # ดึงข้อมูลนักเรียนจาก form และเพิ่ม request quota
        student = Student.objects.get(pk=int(request.POST["student"]))
        QuotaRequest.objects.create(student=student, course=course, status='pending')
        return redirect("courses:course", course_id=course_id)

    return render(request, "courses/request_quota.html", {
        "course": course
    })