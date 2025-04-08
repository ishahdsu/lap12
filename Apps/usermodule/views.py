from django.shortcuts import render
from django.db.models import Count
from .models import address ,student

def task7(request):
    city_counts = address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/task7.html', {'city_counts': city_counts})
