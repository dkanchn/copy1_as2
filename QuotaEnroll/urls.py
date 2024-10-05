from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path("", views.index, name="index"),  # แสดงรายการวิชาทั้งหมด
    path("<int:course_id>", views.enroll_detail, name="enroll_detail"),  # แสดงรายละเอียดวิชาและนักเรียนที่ลงทะเบียน
    path("<int:course_id>/request", views.request_quota, name="request_quota")  # ขอโควต้าลงทะเบียนนักเรียนใหม่
]
