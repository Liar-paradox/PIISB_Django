from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from .models import *
from rest_framework import permissions
from rest_framework.decorators import  api_view, permission_classes
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def view_actors(request):
    db_actor = Aktor.objects.all()
    serializer = Aktorserializer(db_actor, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view_directors(request):
    db_director = Rezyser.objects.all()
    serializer = Rezyserserializer(db_director)
    return Response(serializer.data)

@api_view(['GET'])
def view_film(request):
    db_film = Film.objects.all()
    serializer = Filmserializer(db_film)
    return Response(serializer.data)

@api_view(['GET'])
def view_oceny(request):
    db_oceny = Ocena.objects.all()
    serializer = Ocenaserializer(db_oceny)
    return Response(serializer.data)
