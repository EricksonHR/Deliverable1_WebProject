from django.contrib import admin
from .models import Title, Award, Genre

# Register your models here.
admin.site.register(Title)
admin.site.register(Award)
admin.site.register(Genre)