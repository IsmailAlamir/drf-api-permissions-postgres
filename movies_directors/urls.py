from django.urls import path
from .views import MoviesListView,MoviesDetailView,DirectorListView,DirectorDetailView


urlpatterns = [
   path('', MoviesListView.as_view(), name='movies_list'),
   path('<int:pk>', MoviesDetailView.as_view(),name='movies_detail'),
   path('director/', DirectorListView.as_view(), name='director_list'),
   path('director/<int:pk>', DirectorDetailView.as_view(),name='director_detail'),
]

