from django.urls import path
from . import views

urlpatterns = [
    path('students/city-count', views.task7, name='task7'),
    path('lap9/task1', views.lap9_task1, name='lap9_task1'),
    path('lap9/task2', views.lap9_task2, name='lap9_task2'),
    path('lap9/task3', views.lap9_task3, name='lap9_task3'),
    path('lap9/task4', views.lap9_task4, name='lap9_task4'),
    path('lap11_task1/', views.lap11_task1_student_list, name='student_list'),
    path('lap11_task1/add/', views.lap11_task1_student_add, name='student_add'),
    path('lap11_task1/<int:id>/edit/', views.lap11_task1_student_edit, name='student_edit'),
    path('lap11_task1/<int:id>/delete/', views.lap11_task1_student_delete, name='student_delete'),
    path('lap11_task2/', views.lap11_task2_student_list, name='student2_list'),
    path('lap11_task2/add/', views.lap11_task2_student_add, name='student2_add'),
    path('lap11_task2/<int:id>/edit/', views.lap11_task2_student_edit, name='student2_edit'),
    path('lap11_task2/<int:id>/delete/', views.lap11_task2_student_delete, name='student2_delete'),
    path('lap11_task3/', views.photo_upload, name='photo_upload'),


]

