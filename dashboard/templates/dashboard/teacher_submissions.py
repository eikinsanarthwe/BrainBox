{% extends 'dashboard/base.html' %}
{% load static %}

{% block title %}Submissions - {{ assignment.title }}{% endblock %}

{% block content %}
<div class="container mt-4">
  <h2 class="mb-3">Submissions for "{{ assignment.title }}"</h2>

  <div class="mb-3">
    <a href="{% url 'teacher_assignments' %}" class="btn btn-secondary btn-sm">← Back to assignments</a>
  </div>

  {% if submissions %}
    <div class="table-responsive">
      <table class="table table-striped table-hover align-middle">
        <thead class="table-light">
          <tr>
            <th>Student</th>
            <th>Submitted on</th>
            <th>File / Answer</th>
            <th>Grade</th>
            <th>Feedback</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for sub in submissions %}
            <tr>
              <td>{{ sub.student.user.get_full_name|default:sub.student.user.username }}</td>
              <td>{{ sub.submitted_at|date:"M d, Y H:i" }}</td>
              <td>
                {% if sub.file %}
                  <a href="{{ sub.file.url }}" target="_blank">Download</a>
                {% elif sub.answer %}
                  <span class="text-muted">{{ sub.answer|truncatewords:10 }}</span>
                {% else %}
                  <span class="text-muted">—</span>
                {% endif %}
              </td>
              <td>
                {% if sub.grade %}
                  <span class="badge bg-success">{{ sub.grade }}</span>
                {% else %}
                  <span class="badge bg-warning text-dark">Not graded</span>
                {% endif %}
              </td>
              <td>
                {% if sub.feedback %}
                  {{ sub.feedback|truncatewords:8 }}
                {% else %}
                  <span class="text-muted">—</span>
                {% endif %}
              </td>
              <td>
                <a href="{% url 'grade_submission' sub.id %}" class="btn btn-sm btn-outline-primary">
                  {% if sub.grade %}Update grade{% else %}Grade{% endif %}
                </a>
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  {% else %}
    <div class="alert alert-info">No submissions yet for this assignment.</div>
  {% endif %}
</div>
{% endblock %}
