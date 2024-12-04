from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_disp, name='home_disp'),
    path('addCourse/', views.add_course, name='add_course'),
    path('search/', views.search_course, name='search'),
    path('delete_course/<int:id>', views.delete_course, name='delete_course'),
    path('update_course/<int:id>', views.update_course, name='update_course'),
    path('studentForm/', views.student_form, name='student_form'),
    path('courseForm/', views.course_form_modelform, name='course_form'),
]