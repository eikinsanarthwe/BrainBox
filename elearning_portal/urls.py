from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('teacher/', include(('dashboard.urls_teacher', 'teacher'), namespace='teacher')),
    path('', lambda request: redirect('login')),
]