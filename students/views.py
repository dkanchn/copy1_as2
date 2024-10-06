from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

def student_login(request):
    return render(request, 'students/login.html')

# Define your view for login
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