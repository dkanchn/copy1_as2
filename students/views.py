from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QuotaRequest, Course
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# ฟังก์ชันแสดงหน้า dashboard ของ students หลังจาก login สำเร็จ

def index(request):
    return render(request, 'students/index.html')

@login_required
def student_dashboard(request):
    student = request.user  # ใช้ user ที่ login เข้ามา (ควรเป็น student)
    quota_requests = QuotaRequest.objects.filter(student=student)
    
    return render(request, 'students/dashboard.html', {
        'quota_requests': quota_requests
    })

# ฟังก์ชันสำหรับแสดงรายวิชาที่สามารถขอโควต้าได้
@login_required
def available_courses(request):
    courses = Course.objects.all()
    return render(request, 'students/available_courses.html', {
        'courses': courses
    })

# ฟังก์ชันสำหรับการขอโควต้าในรายวิชา
@login_required
def request_quota(request, course_id):
    student = request.user
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        # ตรวจสอบว่ามีการขอโควต้าสำหรับรายวิชานี้หรือไม่
        existing_request = QuotaRequest.objects.filter(student=student, course=course).first()
        if existing_request:
            messages.error(request, 'คุณได้ทำการขอโควต้าสำหรับรายวิชานี้แล้ว')
        else:
            QuotaRequest.objects.create(student=student, course=course, status='pending')
            messages.success(request, 'ขอโควต้าเรียบร้อยแล้ว')
        return redirect('students:student_dashboard')
    
    return render(request, 'students/request_quota.html', {
        'course': course
    })

# ฟังก์ชันสำหรับดูสถานะการขอโควต้า
@login_required
def quota_status(request):
    student = request.user
    quota_requests = QuotaRequest.objects.filter(student=student)
    
    return render(request, 'students/quota_status.html', {
        'quota_requests': quota_requests
    })

# ฟังก์ชันสำหรับ login ของ students
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # เปลี่ยนไปที่ Dashboard
        else:
            # การจัดการกรณีล็อกอินไม่สำเร็จ
            return render(request, 'students/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'students/login.html')
    
def dashboard(request):
    return render(request, 'students/dashboard.html')