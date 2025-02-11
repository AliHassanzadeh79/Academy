from django.urls import path
from . import views

urlpatterns = [
    path('list' , views.course_list),
    path('standard-list' , views.standard_course_list),
    path('search/<name>' , views.search),
]