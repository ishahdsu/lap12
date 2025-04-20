from django.shortcuts import render
from django.db.models import Count , Min
from .models import address ,student , course , department , studentlap9 , card

def task7(request):
    city_counts = address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/task7.html', {'city_counts': city_counts})



def lap9_task1(request):
    dep_counts = department.objects.annotate(studentlap9_count=Count('studentlap9'))
    return render(request, 'usermodule/lap9_task1.html', {'dep_counts': dep_counts})



def lap9_task2(request):
    course_counts = course.objects.annotate(studentlap9_count=Count('studentlap9'))
    return render(request, 'usermodule/lap9_task2.html', {'course_counts': course_counts})



def lap9_task3(request):
    department_id = department.objects.annotate(studentlap9_oldest=Min('studentlap9'))
    return render(request, 'usermodule/lap9_task3.html', {'department_id': department_id})


def lap9_task4(request):
    dep_counts = department.objects.annotate(studentlap9_count=Count('studentlap9')).filter(studentlap9_count__gt=2).order_by('-studentlap9_count')
    return render(request, 'usermodule/lap9_task1.html', {'dep_counts': dep_counts})