from django.contrib import admin
from .models import Student, Subject, Assignment, Title, Award, Genre

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Title)
admin.site.register(Award)
admin.site.register(Genre)