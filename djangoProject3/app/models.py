from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Subject(models.Model):
    name = models.CharField(max_length=30)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

class Assignment(models.Model):
    name = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    due_date = models.DateField()

    def __str__(self):
        return self.name


class Titles(models.Model):
    title = models.CharField(max_length=100)
    awards = models.ManyToManyField('Awards')
    release_date = models.DateField()
    genre = models.ManyToManyField('Genres')
    producer = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Awards(models.Model):
    award_name = models.CharField(max_length=100)
    award_year = models.IntegerField()

    def __str__(self):
        return self.award_name

class Genres(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name