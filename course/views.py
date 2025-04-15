from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import re
# Create your views here.
courses = [
    {"id": 1, "name": "Python", "capacity": 30, "sessions": 24, "schedule": {"days": ["Saturday", "Monday", "Wednesday"], "time": "10:00-12:00"}, "img_name": "python.jpg", "description": "Learn programming with Python, a versatile and easy-to-use language."},
    {"id": 2, "name": "JavaScript", "capacity": 25, "sessions": 30, "schedule": {"days": ["Sunday", "Tuesday", "Thursday"], "time": "14:00-16:00"}, "img_name": "javascript.jpg", "description": "Master JavaScript, the language for web development and dynamic interactions."},
    {"id": 3, "name": "HTML", "capacity": 20, "sessions": 18, "schedule": {"days": ["Saturday", "Monday", "Wednesday"], "time": "16:00-14:00"}, "img_name": "html.jpg", "description": "Learn HTML, the markup language for structuring web pages."},
    {"id": 4, "name": "Django", "capacity": 15, "sessions": 36, "schedule": {"days": ["Sunday", "Tuesday", "Thursday"], "time": "16:00-18:00"}, "img_name": "django.jpg", "description": "Learn Django, a framework for building web applications with Python."},
    {"id": 5, "name": "CCNA", "capacity": 20, "sessions": 18, "schedule": {"days": ["Saturday", "Monday", "Wednesday"], "time": "08:00-10:00"}, "img_name": "ccna.jpg", "description": "Cisco CCNA course to learn networking fundamentals."},
    {"id": 6, "name": "CCNP", "capacity": 12, "sessions": 15, "schedule": {"days": ["Saturday", "Tuesday"], "time": "09:00-11:00"}, "img_name": "ccnp.jpg", "description": "Advanced Cisco CCNP course for deeper network specialization."}
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
        filter_by_name.extend(courses)
    else:
        # searching
        for course in courses:
            if name.lower() in course['name'].lower():
                filter_by_name.append(course)
            elif name.lower() in course['description'].lower():
                filter_by_name.append(course)
    return render(request, "course/course_list.html" , context={"courses":filter_by_name , "filter_name":name})
    
# def search (request , name):
    # filter_list = [] 
    # response = '<pre style="font-family: Tahoma, Arial, sans-serif; font-size: 14px;">'
    # for course in courses:
    #     if name.lower() in course["name"].lower():
    #         filter_list.append(course)
    #         response = response +'<a href="#">' + ''.join(
    #         f"id: {course['id']}{' ' * (13 - len(str(course['id'])))} , "
    #         f"name: {course['name']}{' ' * (24 - len(course['name']))} , "
    #         f"capacity: {course['capacity']}{' ' * (10 - len(str(course['capacity'])))} , "
    #         f"sessions: {course['sessions']}{' ' * (10 - len(str(course['sessions'])))} , "
    #         f"schedule: {', '.join(course['schedule']['days'])} ({course['schedule']['time']})</a><br/><br/>")
    # response = response + '</pre>'
    # return HttpResponse(response)
    # return render(request,"course/course_list.html" , context={"courses":filter_list})

# def detail (request , id):
#     # filter_id = request.GET.get('id','')
#     filter_id = id
#     if filter_id != '':
#         for course in courses:
#             if course['id'] == int(filter_id) :
#                 filter_name = request.GET.get('filter_name','')
#                 context = course
#                 context.update({"filter_name":filter_name})
#                 return render(request , "course/detail.html" , context=context)   
#     return render(request , "course/404.html")

def detail(request, id):
    filter_id = id
    if filter_id != '':
        for course in courses:
            if course['id'] == int(filter_id):
                context = course.copy()
                filter_name = request.GET.get('filter_name', '')
                if filter_name != "":
                    pattern = re.compile(re.escape(filter_name), re.IGNORECASE) # re.compile('P', re.IGNORECASE)
                    context['description'] = pattern.sub(lambda match: f'<mark>{match.group(0)}</mark>', context['description'])
                return render(request, "course/detail.html", context=context)
    return render(request, "course/404.html")
