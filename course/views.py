from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
course_list = [
    {"id": 1, "name": "Python", "capacity": 30, "sessions": 24, "schedule": {"days": ["شنبه", "دوشنبه", "چهارشنبه"], "time": "10:00-12:00"}},
    {"id": 2, "name": "JavaScript", "capacity": 25, "sessions": 30, "schedule": {"days": ["یکشنبه", "سه شنبه", "پنج شنبه"], "time": "14:00-16:00"}},
    {"id": 3, "name": "HTML", "capacity": 20, "sessions": 18, "schedule": {"days": ["شنبه", "دوشنبه", "چهارشنبه"], "time": "12:00-14:00"}},
    {"id": 4, "name": "Django", "capacity": 15, "sessions": 36, "schedule": {"days": ["یکشنبه", "سه شنبه", "پنج شنبه"], "time": "16:00-18:00"}},
    {"id": 5, "name": "CSS", "capacity": 20, "sessions": 18, "schedule": {"days": ["شنبه", "دوشنبه", "چهارشنبه"], "time": "08:00-10:00"}}
]

def courses(request):
    response = ''.join(
        f"id: {course['id']} , name: {course['name']} , capacity: {course['capacity']} , sessions: {course['sessions']} , schedule: {', '.join(course['schedule']['days'])} ({course['schedule']['time']})<br/>"
        for course in course_list
    )
    return HttpResponse(response)
