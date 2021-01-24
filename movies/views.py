from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Movie
from .serializers import MovieSerializer

# Movie API View
class MovieListAPIView(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

