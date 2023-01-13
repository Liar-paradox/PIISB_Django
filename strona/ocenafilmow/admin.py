from django.contrib import admin
from .models import Aktor,Rezyser,Film,Ocena
# Register your models here.


#Rejestrowanie w admin panelu modeli Aktor, Film i Rezyser
class FilmAdmin(admin.ModelAdmin):
    list_display = ('nazwa','opis','show_actors','show_directors')

    def show_actors(self, obj):
        return "\n".join([f'{a.imie} {a.nazwisko}' for a in obj.aktor.all()])

    def show_directors(self,obj):
        return "\n".join([f'{a.imie} {a.nazwisko}' for a in obj.aktor.all()])

class AktorAdmin(admin.ModelAdmin):
    list_display = ('imie','nazwisko')

class RezyserAdmin(admin.ModelAdmin):
    list_display = ('imie','nazwisko')

admin.site.register(Aktor, AktorAdmin)
admin.site.register(Rezyser, RezyserAdmin)
admin.site.register(Film,FilmAdmin)
admin.site.register(Ocena)


