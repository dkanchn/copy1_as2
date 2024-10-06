from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),  # กำหนดหน้าแรกของแอป students
    path('request-quota/', views.request_quota, name='request_quota'),
    path('quota-status/', views.quota_status, name='quota_status'),
    path('login/', views.student_login, name='login'),
]