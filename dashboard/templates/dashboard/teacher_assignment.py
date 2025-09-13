{% extends 'dashboard/base.html' %}
{% load static %}

{% block title %}My Assignments{% endblock %}

{% block content %}
<div class="container mt-4">
  <h2 class="mb-3">My Assignments</h2>

  {% if assignments %}
    <div class="table-responsive">
      <table class="table table-striped table-hover align-middle">
        <thead class="table-light">
          <tr>
            <th>Title</th>
            <th>Course</th>
            <th>Created</th>
            <th>Due date</th>
            <th>Submissions</th>
          </tr>
        </thead>
        <tbody>
          {% for a in assignments %}
            <tr>
              <td>
                <a href="{% url 'teacher_submissions' a.id %}">{{ a.title }}</a>
              </td>
              <td>{{ a.course.title }}</td>
              <td>{{ a.created_at|date:"M d, Y" }}</td>
              <td>{{ a.due_date|date:"M d, Y" }}</td>
              <td>
                <a href="{% url 'teacher_submissions' a.id %}" class="btn btn-sm btn-outline-primary">
                  View submissions
                </a>
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  {% else %}
    <div class="alert alert-info">No assignments created yet.</div>
  {% endif %}

  <div class="mt-3">
    <a href="{% url 'teacher_dashboard' %}" class="btn btn-secondary">Back to dashboard</a>
  </div>
</div>
{% endblock %}
