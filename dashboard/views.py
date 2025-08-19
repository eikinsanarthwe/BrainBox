from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Teacher, Student, Assignment, Course
from .forms import TeacherForm, StudentForm, CourseForm, AssignmentForm

# Dashboard View
def dashboard(request):
    context = {
        'teacher_count': Teacher.objects.count(),
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
        'pending_assignments': Assignment.objects.filter(status='pending').count(),
    }
    return render(request, 'dashboard/index.html', context)

# Teacher Views
def teacher_list(request):
    teachers = Teacher.objects.all().select_related('user')
    return render(request, 'dashboard/teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    return edit_teacher(request)

def edit_teacher(request, id=None):
    teacher = get_object_or_404(Teacher, id=id) if id else None
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            teacher = form.save()
            return redirect('dashboard:teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    
    return render(request, 'dashboard/teacher_form.html', {
        'form': form,
        'title': 'Edit Teacher' if id else 'Add Teacher'
    })

def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect('dashboard:teacher_list')

# Student Views
def student_list(request):
    students = Student.objects.all().select_related('user')
    return render(request, 'dashboard/student_list.html', {'students': students})

def student_create(request):
    return edit_student(request)

def edit_student(request, id=None):
    student = get_object_or_404(Student, id=id) if id else None
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('dashboard:student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'dashboard/student_form.html', {
        'form': form,
        'title': 'Edit Student' if id else 'Add Student'
    })

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('dashboard:student_list')

# Course Views
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'dashboard/course_list.html', {'courses': courses})

def course_create(request):
    return edit_course(request)

def edit_course(request, id=None):
    course = get_object_or_404(Course, id=id) if id else None
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('dashboard:course_list')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'dashboard/course_form.html', {
        'form': form,
        'title': 'Edit Course' if id else 'Add Course'
    })

def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('dashboard:course_list')

# Assignment Views
def assignment_list(request):
    assignments = Assignment.objects.all().select_related('course', 'teacher')
    return render(request, 'dashboard/assignment_list.html', {'assignments': assignments})

def assignment_create(request):
    return edit_assignment(request)

def edit_assignment(request, id=None):
    assignment = get_object_or_404(Assignment, id=id) if id else None
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            assignment = form.save()
            return redirect('dashboard:assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    
    return render(request, 'dashboard/assignment_form.html', {
        'form': form,
        'title': 'Edit Assignment' if id else 'Add Assignment'
    })

def delete_assignment(request, id):
    assignment = get_object_or_404(Assignment, id=id)
    assignment.delete()
    return redirect('dashboard:assignment_list')