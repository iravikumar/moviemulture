from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Movie, MovieList
from .serializers import MovieSerializer, MovieListSerializer

# Movie API View
class MovieListAPIView(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# MovieList API View
class MovieListListAPIView(ListCreateAPIView):

    queryset = MovieList.objects.all()
    serializer_class = MovieListSerializer


class MovieListDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = MovieList.objects.all()
    serializer_class = MovieListSerializer