from django.db import models


# Create your models here.


class Title(models.Model):
    title = models.CharField(max_length=100)
    award = models.ManyToManyField('Award')
    release_date = models.DateField()
    genre = models.ManyToManyField('Genre')
    producer = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Award(models.Model):
    award_name = models.CharField(max_length=100)
    award_year = models.IntegerField()

    def __str__(self):
        return self.award_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name

