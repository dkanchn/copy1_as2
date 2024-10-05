from django.shortcuts import render, redirect

# Create your views here.
from .models import Course, Student, Enroll

def index(request):
    # ดึงวิชาทั้งหมดที่เปิดให้ลงทะเบียน
    courses = Course.objects.all()
    return render(request, "courses/index.html", {
        "courses": courses
    })
    
    
def enroll_detail(request, course_id):
    # ดึงรายละเอียดของวิชาที่เลือก
    course = Course.objects.get(pk=course_id)
    enrolled_students_count = course.students.count()
    available_seats = course.seats - enrolled_students_count
    
    return render(request, "courses/enroll_detail.html", {
        "course": course,
        "enrolled_students_count": enrolled_students_count,
        "available_seats": available_seats
    })
    
    
def request_quota(request, course_id):
    # ตรวจสอบว่ายังมีที่นั่งว่างสำหรับลงทะเบียนหรือไม่
    course = Course.objects.get(pk=course_id)
    enrolled_students_count = course.students.count()
    
    if enrolled_students_count < course.seats:
        # เพิ่มนักเรียนใหม่ในวิชานี้
        student = Student.objects.get(pk=1)  # ตัวอย่าง: ดึงข้อมูลนักเรียนจาก ID (ปรับได้ตามความต้องการ)
        Enroll.objects.create(student=student, course=course)
        return redirect("courses:enroll_detail", course_id=course_id)
    
    # หากที่นั่งเต็มแล้ว ให้กลับไปที่หน้าเดิมพร้อมแสดงข้อความแจ้ง
    return render(request, "courses/enroll_detail.html", {
        "course": course,
        "error_message": "No available seats in this course."
    })