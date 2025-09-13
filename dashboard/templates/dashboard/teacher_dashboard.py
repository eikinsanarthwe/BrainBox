{% extends 'dashboard/base.html' %}
{% load static %}

{% block title %}Teacher Dashboard{% endblock %}

{% block content %}
<div class="container mt-4">
  <div class="d-flex justify-content-between align-items-center mb-3">
    <div>
      <h1 class="h3 mb-0">Welcome, {{ teacher.user.get_full_name|default:teacher.user.username }}</h1>
      <div class="text-muted small">Teacher portal</div>
    </div>
    <div>
      <a href="{% url 'teacher_profile' %}" class="btn btn-outline-primary btn-sm me-2">Profile</a>
      <a href="/dashboard/" class="btn btn-outline-secondary btn-sm">Admin</a>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-8">
      <!-- Courses card -->
      <div class="card mb-3">
        <div class="card-header"><strong>Your courses</strong></div>
        <div class="card-body p-0">
          {% if courses %}
            <ul class="list-group list-group-flush">
              {% for course in courses %}
                <li class="list-group-item d-flex justify-content-between align-items-center">
                  <div>
                    <a href="{% url 'teacher_course_detail' course.id %}" class="fw-bold">{{ course.title }}</a>
                    <div class="text-muted small">
                      {{ course.code|default:"" }}{% if course.semester %} — {{ course.semester }}{% endif %}
                    </div>
                  </div>
                  <a href="{% url 'teacher_course_detail' course.id %}" class="btn btn-sm btn-outline-primary">Open</a>
                </li>
              {% endfor %}
            </ul>
          {% else %}
            <div class="p-3 text-muted">You don't have any courses assigned yet.</div>
          {% endif %}
        </div>
      </div>

      <!-- Recent assignments -->
      <div class="card">
        <div class="card-header"><strong>Recent assignments</strong></div>
        <div class="card-body">
          {% if assignments %}
            <div class="table-responsive">
              <table class="table table-sm mb-0">
                <thead>
                  <tr>
                    <th>Title</th>
                    <th>Course</th>
                    <th>Due</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  {% for a in assignments %}
                    <tr>
                      <td><a href="{% url 'teacher_submissions' a.id %}">{{ a.title }}</a></td>
                      <td>{{ a.course.title }}</td>
                      <td>{{ a.due_date|date:"M d, Y" }}</td>
                      <td><a class="btn btn-sm btn-outline-secondary" href="{% url 'teacher_submissions' a.id %}">Submissions</a></td>
                    </tr>
                  {% endfor %}
                </tbody>
              </table>
            </div>
          {% else %}
            <div class="text-muted">No recent assignments found.</div>
          {% endif %}
        </div>
      </div>
    </div>

    <div class="col-lg-4">
      <div class="card mb-3">
        <div class="card-header"><strong>Quick actions</strong></div>
        <div class="card-body">
          <a href="{% url 'teacher_assignments' %}" class="btn btn-primary w-100 mb-2">Manage assignments</a>
          <a href="{% url 'teacher_profile' %}" class="btn btn-outline-primary w-100 mb-2">Edit profile</a>
          <a href="/dashboard/" class="btn btn-outline-secondary w-100">Open admin dashboard</a>
        </div>
      </div>

      <div class="card">
        <div class="card-header"><strong>Contact</strong></div>
        <div class="card-body">
          <p class="mb-1"><strong>Email</strong><br>{{ teacher.user.email }}</p>
          {% if teacher.phone %}
            <p class="mb-0"><strong>Phone</strong><br>{{ teacher.phone }}</p>
          {% endif %}
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
