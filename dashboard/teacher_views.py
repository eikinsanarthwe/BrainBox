from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def teacher_dashboard(request):
    """Teacher portal home."""
    # Import here to avoid circular import
    from .models import Teacher, Course, Assignment, Submission
    
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "You are not registered as a teacher.")
        return redirect('login')
    
    courses = Course.objects.filter(teachers=teacher)
    assignments = Assignment.objects.filter(teacher=request.user).order_by('-due_date')[:5]
    
    # Count submissions that need grading (no grade assigned yet)
    pending_grading_count = Submission.objects.filter(
        assignment__teacher=request.user,
        grade__isnull=True
    ).count()
    
    return render(request, 'dashboard/teacher_dashboard.html', {
        'teacher': teacher,
        'courses': courses,
        'assignments': assignments,
        'pending_grading_count': pending_grading_count,
        'now': timezone.now(),
    })

@login_required
def teacher_assignments(request):
    """List assignments created by this teacher."""
    # Import here to avoid circular import
    from .models import Teacher, Assignment
    
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "You are not registered as a teacher.")
        return redirect('login')
        
    # Get filter parameter
    status_filter = request.GET.get('status', 'all')
    
    # Base queryset
    assignments = Assignment.objects.filter(teacher=request.user)
    
    # Apply filter if specified
    if status_filter != 'all':
        assignments = assignments.filter(status=status_filter)
    
    assignments = assignments.order_by('-created_at')
    
    return render(request, 'dashboard/teacher_assignments.html', {
        'teacher': teacher,
        'assignments': assignments,
        'now': timezone.now(),
    })

@login_required
def create_assignment(request):
    """Create a new assignment."""
    # Import here to avoid circular import
    from .models import Teacher, Course, Student
    from .forms import AssignmentForm
    
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "You are not registered as a teacher.")
        return redirect('login')
        
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.teacher = request.user
            assignment.save()
            form.save_m2m()  # Save many-to-many data
            messages.success(request, "Assignment created successfully!")
            return redirect('teacher:teacher_assignments')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AssignmentForm()
        # Filter courses to only those taught by this teacher
        form.fields['course'].queryset = Course.objects.filter(teachers=teacher)
        # Filter students to only those in the teacher's courses
        form.fields['students'].queryset = Student.objects.filter(
            course__in=Course.objects.filter(teachers=teacher)
        ).distinct()
    
    return render(request, 'dashboard/assignment_form.html', {
        'form': form,
        'title': 'Create Assignment'
    })

@login_required
def teacher_submissions(request, assignment_id):
    """View submissions for a specific assignment."""
    # Import here to avoid circular import
    from .models import Teacher, Assignment, Submission
    
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "You are not registered as a teacher.")
        return redirect('login')
        
    assignment = get_object_or_404(Assignment, id=assignment_id, teacher=request.user)
    submissions = Submission.objects.filter(assignment=assignment)
    
    return render(request, 'dashboard/teacher_submissions.html', {
        'teacher': teacher,
        'assignment': assignment,
        'submissions': submissions,
    })

@login_required
def grade_submission(request, submission_id):
    """Grade a student's submission."""
    # Import here to avoid circular import
    from .models import Teacher, Submission
    
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "You are not registered as a teacher.")
        return redirect('login')
        
    submission = get_object_or_404(
        Submission, 
        id=submission_id, 
        assignment__teacher=request.user
    )

    if request.method == 'POST':
        grade = request.POST.get('grade')
        feedback = request.POST.get('feedback')
        
        if grade:
            try:
                submission.grade = int(grade)
                submission.feedback = feedback
                submission.save()
                messages.success(request, "Submission graded successfully.")
                return redirect('teacher:teacher_submissions', assignment_id=submission.assignment.id)
            except ValueError:
                messages.error(request, "Please enter a valid grade.")
    
    return render(request, 'dashboard/grade_submission.html', {
        'teacher': teacher,
        'submission': submission,
        'max_points': submission.assignment.max_points
    })

@login_required
def teacher_courses(request):
    """View all courses taught by this teacher."""
    # Import here to avoid circular import
    from .models import Teacher, Course
    
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "You are not registered as a teacher.")
        return redirect('login')
        
    courses = Course.objects.filter(teachers=teacher)
    
    return render(request, 'dashboard/teacher_courses.html', {
        'teacher': teacher,
        'courses': courses,
    })