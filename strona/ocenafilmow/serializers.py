from .models import *
from rest_framework import serializers

class Aktorserializer(serializers.ModelSerializer):
    class Meta:
        model = Aktor
        fields = '__all__'

class Rezyserserializer(serializers.ModelSerializer):
    class Meta:
        model = Rezyser
        fields = "__all__"

class Filmserializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class Ocenaserializer(serializers.ModelSerializer):
    class Meta:
        model = Ocena
        fields = '__all__'
