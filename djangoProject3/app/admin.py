from django.contrib import admin
from .models import Student, Subject, Assignment, Titles, Awards, Genres

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Titles)
admin.site.register(Awards)
admin.site.register(Genres)