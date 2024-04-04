from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse


# from .models import Student

# Create your views here.

def hello_world(request):
    # return HttpResponse("Hello world!")
    return render(request, 'hello_world.html')

def login(request):
    # return HttpResponse("Hello world!")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página después del registro exitoso
            return redirect('login')  # Redirigir a la página de inicio de sesión
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def welcome(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página después del registro exitoso
            return redirect('login')  # Redirigir a la página de inicio de sesión
    else:
        form = UserCreationForm()
    return render(request, 'welcome.html', {'form': form})

'''
def get_students(request):
    students = Student.objects.all()
    student_values = list(students.values())
    return JsonResponse(student_values, safe=False)
'''
