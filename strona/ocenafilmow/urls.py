from django.urls import path
from . import views

urlpatterns = [
    path('aktorzy/',views.view_actors),
    path('rezyserzy/',views.view_directors),
    path('filmy/',views.view_film),
    path('oceny/',views.view_oceny),
]
