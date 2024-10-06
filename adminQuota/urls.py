from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('courses/', views.course, name='manage_courses'),
    path('quota-requests/', views.request_quota, name='manage_quotas'),
    path('login/', views.user_login, name='login'),
]