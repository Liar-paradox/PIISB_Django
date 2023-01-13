from django.db import models
from django.utils.text import slugify
import datetime

# Create your models here.
class Aktor(models.Model):
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.imie, self.nazwisko}"

class Rezyser(models.Model):
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.imie, self.nazwisko}"

class Ocena(models.Model):
    ocena = models.IntegerField()
    wartosc = models.IntegerField()

    def __str__(self):
        return f"Ocena:{self.ocena} Wartość:{self.wartosc}"

class Film(models.Model):
    nazwa = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100,null=True,editable=False)
    opis = models.TextField(max_length=400)
    aktor = models.ManyToManyField(Aktor)
    rezyser = models.ManyToManyField(Rezyser)
    #Dodać srednia ocen wczytaj oceny i wyliczyc srednia srednia

    def __str__(self):
        return self.nazwa



