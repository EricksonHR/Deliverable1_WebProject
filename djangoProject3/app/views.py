from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# from .models import Student

# Create your views here.

def hello_world(request):
    # return HttpResponse("Hello world!")
    return render(request, 'hello_world.html')


'''
def get_students(request):
    students = Student.objects.all()
    student_values = list(students.values())
    return JsonResponse(student_values, safe=False)
'''
