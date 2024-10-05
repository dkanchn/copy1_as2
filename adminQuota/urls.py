from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('courses/', views.manage_courses, name='manage_courses'),
    path('quota-requests/', views.manage_quotas, name='manage_quotas'),
]