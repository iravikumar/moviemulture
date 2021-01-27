import uuid
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):

    imdb_title_id = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    original_title = models.CharField(max_length=256, blank=True, null=True)
    year = models.CharField(max_length=32, blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=128, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    language = models.CharField(max_length=128, blank=True, null=True)
    director = models.CharField(max_length=128, blank=True, null=True)
    writer = models.CharField(max_length=256, blank=True, null=True)
    production_company = models.CharField(max_length=256, blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    avg_vote = models.FloatField(blank=True, null=True)
    votes = models.FloatField(blank=True, null=True)
    budget = models.CharField(max_length=56, blank=True, null=True)
    usa_gross_income = models.CharField(max_length=56, blank=True, null=True)
    worlwide_gross_income = models.CharField(max_length=56, blank=True, null=True)
    metascore = models.FloatField(blank=True, null=True)
    reviews_from_users = models.FloatField(blank=True, null=True)
    reviews_from_critics = models.FloatField(blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Movies'


    def __str__(self):
        return self.title if self.title else self.id



class MovieList(models.Model):

    list_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, blank=True)
    movies = models.ManyToManyField(Movie, related_name='movies', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


    class Meta:
        verbose_name_plural = 'MovieList'


    def __str__(self):
        return self.name if self.name else self.id