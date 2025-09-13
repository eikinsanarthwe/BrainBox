from django.urls import path
from . import teacher_views

app_name = 'teacher'  # This defines the namespace

urlpatterns = [
    path('', teacher_views.teacher_dashboard, name='teacher_dashboard'),
    path('assignments/', teacher_views.teacher_assignments, name='teacher_assignments'),
    path('assignments/create/', teacher_views.create_assignment, name='assignment_create'),
    path('assignments/<int:assignment_id>/submissions/', 
         teacher_views.teacher_submissions, name='teacher_submissions'),
    path('courses/', teacher_views.teacher_courses, name='teacher_courses'),
    path('submissions/<int:submission_id>/grade/', 
         teacher_views.grade_submission, name='grade_submission'),
]