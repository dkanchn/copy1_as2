from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check if the user is an admin
            if user.is_superuser:
                return redirect('dashboard')  # Redirect admin to their dashboard
            
            # Check if the user is a student (for example, check if they belong to the 'student' group)
            elif user.groups.filter(name='student').exists():
                return redirect('student_dashboard')  # Redirect students to their dashboard
            
            # Default: if no role found, redirect to the homepage
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

# Example view for student dashboard (you should define this in your urls.py)
@login_required
def student_dashboard(request):
    return render(request, 'students/dashboard.html')

# Example view for admin dashboard (you should define this in your urls.py)
@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')