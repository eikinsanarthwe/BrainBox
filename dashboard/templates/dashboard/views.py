from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Optional: restrict access to admins only
def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@user_passes_test(is_admin)
def admin_home(request):
    return render(request, 'dashboard/admin_home.html')

@user_passes_test(is_admin)
def course_list(request):
    return render(request, 'dashboard/course_list.html')

@user_passes_test(is_admin)
def course_form(request):
    return render(request, 'dashboard/course_form.html')

@user_passes_test(is_admin)
def student_list(request):
    return render(request, 'dashboard/student_list.html')

@user_passes_test(is_admin)
def student_form(request):
    return render(request, 'dashboard/student_form.html')

@user_passes_test(is_admin)
def teacher_list(request):
    return render(request, 'dashboard/teacher_list.html')

@user_passes_test(is_admin)
def teacher_form(request):
    return render(request, 'dashboard/teacher_form.html')

@user_passes_test(is_admin)
def assignment(request):
    return render(request, 'dashboard/assignment.html')

@user_passes_test(is_admin)
def assignment_form(request):
    return render(request, 'dashboard/assignment_form.html')

@login_required
@user_passes_test(is_admin)
def index(request):
    return render(request, 'dashboard/index.html')


