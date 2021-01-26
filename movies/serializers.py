from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Movie, MovieList


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    # movies = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all(),  many=True, required=False)

    class Meta:
        model = MovieList
        fields = '__all__'

