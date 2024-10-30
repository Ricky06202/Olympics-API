from django.db import models

class OlympicsData(models.Model):
    City = models.TextField(max_length=200)
    Year = models.IntegerField()
    Sport = models.TextField(max_length=200)
    Discipline = models.TextField(max_length=200)
    Event = models.TextField(max_length=200)
    Athlete = models.TextField(max_length=200)
    Gender = models.TextField(max_length=200)
    Country_Code = models.TextField(max_length=3)
    Country = models.TextField(max_length=200)
    Event_gender = models.TextField(max_length=1)
    Medal = models.TextField(max_length=100)
