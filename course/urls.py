from django.urls import path
from . import views

urlpatterns = [
    path('list' , views.course_list),
    path('standard-list' , views.standard_course_list , name="course-list"),
    path('detail/<int:id>' , views.detail , name="course-detail"),
    # path('search/<name>' , views.search),
]