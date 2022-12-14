from rest_framework import serializers

from .models import Movie,Director

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields='__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Director
        fields='__all__'
