from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from .forms import StudentForm, CourseForm

# Create your views here.


def home_disp(request):
    return render(request, 'home.html')


def add_course(request):
    if request.method == 'POST':

        course_name = request.POST['course_name']
        course_details = request.POST['course_details']
        course_duration = request.POST['course_duration']

        course = Course(course=course_name, content=course_details, duration=course_duration)
        course.save()

        #Course.objects.create(course=course_name,content=course_details,duration=course_duration,)
        return redirect('/addCourse/')

    course_queryset = Course.objects.all()
    context = {'data': course_queryset}

    return render(request, 'course_content.html', context)


def search_course(request):
    course_queryset = Course.objects.all()
    context = {'data': course_queryset}

    dict_search = request.GET
    course_nm = dict_search.get('search')
    if course_nm:
        searchedData = course_queryset.filter(course=course_nm)
        context = {'data': searchedData}

    return render(request, 'search.html', context)

def delete_course(request,id):

    query_data = Course.objects.get(id=id)
    query_data.delete()
    course_data = Course.objects.all()
    context = {'data': course_data}

    return render(request, 'search.html', context)


def update_course(request, id):
    query_data1 = Course.objects.get(id=id)
    dict = {'data': query_data1}
    print(query_data1)
    if request.method == 'POST':
        course_name = request.POST['course_name']
        course_details = request.POST['course_details']
        course_duration = request.POST['course_duration']
        query_data1.course = course_name
        query_data1.content = course_details
        query_data1.duration = course_duration
        query_data1.save()
        return redirect('/search/')
    return render(request, 'update_course.html', dict)


def student_form(request):
    context = {}
    context['form'] = StudentForm()
    return render(request, "student_form.html", context)


def course_form_modelform(request):

    context ={}
    context['form'] = CourseForm()
    return render(request, "course_form_modelforms.html", context)













