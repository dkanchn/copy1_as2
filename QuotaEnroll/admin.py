from django.contrib import admin
from .models import Course, Student, Enroll

class StudentAdmin(admin.ModelAdmin):
    # ลบ filter_horizontal หรือใช้กับฟิลด์อื่นที่ไม่มีโมเดลตัวกลาง
    pass

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "course_code", "course_name", "semester", "year", "seats")

class EnrollAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "date_enrolled")

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enroll, EnrollAdmin)