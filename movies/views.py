from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

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


class MovieRecommendationsAPIView(APIView):

    def get(self, request):
        try:
            list_id = self.request.query_params.get('list_id')

            if list_id:
                movie_list = MovieList.objects.filter(list_id=list_id).first()
                if movie_list:
                    serialized_movie_list = MovieListSerializer(movie_list)
                    movie_ids = serialized_movie_list.data.pop('movies', [])

                    movie_years = {Movie.objects.get(id=movie_id).year for movie_id in movie_ids}

                    movie_recommendations = Movie.objects.filter(year__in=movie_years).order_by('year')
                    serialized_movie_recommendations = MovieSerializer(movie_recommendations,  many=True)

                    return Response(serialized_movie_recommendations.data, , status=status.HTTP_200_OK)

            return Response({"message": "Wrong list_id"})

        except MovieList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        serializer = MovieListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
