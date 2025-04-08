from django.urls import path
from . import views

urlpatterns = [
    path('students/city-count', views.task7, name='task7'),

]

