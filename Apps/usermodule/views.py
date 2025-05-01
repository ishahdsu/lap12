from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count , Min
from .models import address ,student , course , department , studentlap9 , card , student2
from .forms import StudentForm , Student2Form , PhotoForm , SignUpForm
from django.contrib.auth import logout ,login
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages



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


from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login/')
def lap11_task1_student_list(request):
    students = student.objects.all()
    return render(request, 'usermodule/lap11_task1/student_list.html', {'students': students})


def lap11_task1_student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'usermodule/lap11_task1/student_form.html', {'form': form})

def lap11_task1_student_edit(request, id):
    stu = student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=stu)
    return render(request, 'usermodule/lap11_task1/student_form.html', {'form': form})

def lap11_task1_student_delete(request, id):
    stu = student.objects.get(id=id)
    if request.method == 'POST':
        stu.delete()
        return redirect('student_list')
    return render(request, 'usermodule/lap11_task1/student_delete.html', {'student': stu})



def lap11_task2_student_list(request):
    students = student2.objects.all()
    return render(request, 'usermodule/lap11_task2/student2_list.html', {'students': students})

def lap11_task2_student_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
    return render(request, 'usermodule/lap11_task2/student2_form.html', {'form': form})

def lap11_task2_student_edit(request, id):
    stu = student2.objects.get(id=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form(instance=stu)
    return render(request, 'usermodule/lap11_task2/student2_form.html', {'form': form})

def lap11_task2_student_delete(request,id):
    stu = student2.objects.get(id=id)
    if request.method == 'POST':
        stu.delete()
        return redirect('student2_list')
    return render(request, 'usermodule/lap11_task2/student2_delete.html', {'student': stu})



def photo_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('photo_upload') 
    else:
        form = PhotoForm()
    return render(request, 'usermodule/photo_upload.html', {'form': form})


def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered.")  # Optional success message
            return redirect('login')
    else:
        form = SignUpForm()  # This ensures 'form' is always defined

    return render(request, "usermodule/register.html", {"form": form})

def logoutUser(request):
    logout(request)
    return redirect('task7') 

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")  
            return redirect('student_list')
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, "usermodule/login.html", {"form": form})









