from django import forms
from django.contrib.auth import get_user_model
from .models import Teacher, Student, Course,Assignment
User = get_user_model()

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'specialty', 'phone']
        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select user account'
            }),
            'specialty': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Mathematics, Physics'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1234567890'
            })
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'enrollment_id', 'course']
        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select user account'
            }),
            'enrollment_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter enrollment ID'
            }),
            'course': forms.Select(attrs={
                'class': 'form-control'
            })
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'description', 'teachers']  # Added 'teachers' field
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. CS101'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Introduction to Computer Science'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Course description...'
            }),
            'teachers': forms.SelectMultiple(attrs={
                'class': 'form-control select2-multiple',
                'data-placeholder': 'Select teachers...'
            })
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'teacher', 'max_points']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter assignment title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Detailed assignment description...'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'course': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select course'
            }),
            'teacher': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select teacher'
            }),
            'max_points': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maximum score (e.g. 100)',
                'min': 1
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If you want to filter teachers based on selected course (optional)
        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['teacher'].queryset = Teacher.objects.filter(courses_taught=course_id)
            except (ValueError, TypeError):
                pass