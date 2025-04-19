from django.urls import path
from . import views

urlpatterns = [
    path('students/city-count', views.task7, name='task7'),
    path('lap9/task1', views.lap9_task1, name='lap9_task1'),
    path('lap9/task2', views.lap9_task2, name='lap9_task2'),
    path('lap9/task3', views.lap9_task3, name='lap9_task3'),
    path('lap9/task4', views.lap9_task4, name='lap9_task4'),


    

]

