from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
courses = [
    {"id": 1, "name": "Python", "capacity": 30, "sessions": 24, "schedule": {"days": ["Saturday", "Monday", "Wednesday"], "time": "10:00-12:00"}},
    {"id": 2, "name": "JavaScript", "capacity": 25, "sessions": 30, "schedule": {"days": ["Sunday", "Tuesday", "Thursday"], "time": "14:00-16:00"}},
    {"id": 3, "name": "HTML", "capacity": 20, "sessions": 18, "schedule": {"days": ["Saturday", "Monday", "Wednesday"], "time": "16:00-14:00"}},
    {"id": 4, "name": "Django", "capacity": 15, "sessions": 36, "schedule": {"days": ["Sunday", "Tuesday", "Thursday"], "time": "16:00-18:00"}},
    {"id": 5, "name": "CCNA", "capacity": 20, "sessions": 18, "schedule": {"days": ["Saturday", "Monday", "Wednesday"], "time": "08:00-10:00"}},
    {"id": 6, "name": "CCNP", "capacity": 12, "sessions": 15, "schedule": {"days": ["Saturday", "Tuesday"], "time": "09:00-11:00"}},
]

def course_list(request):
    response = "<pre style='font-family: Tahoma, Arial, sans-serif; font-size: 14px;'>"
    for course in courses:
        url = reverse("course-detail" , args=[course['id']])
        response += f"id: {course['id']}{' ' * (13 - len(str(course['id'])))} , "
        response += f"name:<a href='{url}'>{course['name']}</a>{' ' * (24 - len(course['name']))} , "
        response += f"capacity: {course['capacity']}{' ' * (10 - len(str(course['capacity'])))} , "
        response += f"sessions: {course['sessions']}{' ' * (10 - len(str(course['sessions'])))} , "
        response += f"schedule: {', '.join(course['schedule']['days'])} ({course['schedule']['time']})<br/>"
    response += '</pre>'
    return HttpResponse(response)

def standard_course_list(request):
    filter_by_name = []
    name = request.GET.get('name','')
    if name == '':
        return render(request,"course/course_list.html" , context={"courses":courses})
    else:
        for course in courses:
            if name.lower() in course['name'].lower():
                filter_by_name.append(course)
        return render(request, "course/course_list.html" , context={"courses":filter_by_name})
    
def search (request , name):
    filter_list = [] 
    response = '<pre style="font-family: Tahoma, Arial, sans-serif; font-size: 14px;">'
    for course in courses:
        if name.lower() in course["name"].lower():
            filter_list.append(course)
    #         response = response +'<a href="#">' + ''.join(
    #         f"id: {course['id']}{' ' * (13 - len(str(course['id'])))} , "
    #         f"name: {course['name']}{' ' * (24 - len(course['name']))} , "
    #         f"capacity: {course['capacity']}{' ' * (10 - len(str(course['capacity'])))} , "
    #         f"sessions: {course['sessions']}{' ' * (10 - len(str(course['sessions'])))} , "
    #         f"schedule: {', '.join(course['schedule']['days'])} ({course['schedule']['time']})</a><br/><br/>")
    # response = response + '</pre>'
    # return HttpResponse(response)
    return render(request,"course/course_list.html" , context={"courses":filter_list})

def detail (request , id):
    # filter_id = request.GET.get('id','')
    filter_id = id
    if filter_id != '':
        for course in courses:
            if course['id'] == int(filter_id) :
                return render(request , "course/detail.html" , context=course)   
    return render(request , "course/404.html")


