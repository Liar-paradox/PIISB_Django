from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from .models import *
from rest_framework import permissions, viewsets
from rest_framework.decorators import  api_view, permission_classes
from rest_framework.response import Response
# Create your views here.

class view_actors(viewsets.ModelViewSet):
    queryset = Aktor.objects.all()
    serializer_class = Aktorserializer
    permission_classes = [permissions.IsAuthenticated]

class view_directors(viewsets.ModelViewSet):
    queryset = Rezyser.objects.all()
    serializer_class = Rezyserserializer
    permission_classes = [permissions.IsAuthenticated]

class view_film(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = Filmserializer
    permission_classes = [permissions.IsAuthenticated]

class view_oceny(viewsets.ModelViewSet):
    queryset = Ocena.objects.all()
    serializer_class = Ocenaserializer
    permission_classes = [permissions.IsAuthenticated]
