from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import MovieSerializer,DirectorSerializer
from .models import Movie,Director
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly




class MoviesListView(ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class= MovieSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]



class MoviesDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class= MovieSerializer
    permission_classes=[IsOwnerOrReadOnly]


class DirectorListView(ListCreateAPIView):
    queryset=Director.objects.all()
    serializer_class= DirectorSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]


class DirectorDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Director.objects.all()
    serializer_class= DirectorSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]