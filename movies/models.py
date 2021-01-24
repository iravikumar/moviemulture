from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):

    imdb_title_id = models.CharField(max_length=32, blank=True)
    title = models.CharField(max_length=256, blank=True)
    original_title = models.CharField(max_length=256, blank=True)
    year = models.CharField(max_length=32, blank=True)
    date_published = models.DateField()
    genre = models.CharField(max_length=128, blank=True)
    duration = models.FloatField(blank=True)
    country = models.CharField(max_length=128, blank=True)
    language = models.CharField(max_length=128, blank=True)
    director = models.CharField(max_length=128, blank=True)
    writer = models.CharField(max_length=256, blank=True)
    production_company = models.CharField(max_length=256, blank=True)
    actors = models.TextField(blank=True)
    description = models.TextField(blank=True)
    avg_vote = models.FloatField(blank=True)
    votes = models.FloatField(blank=True)
    budget = models.CharField(max_length=56, blank=True)
    usa_gross_income = models.CharField(max_length=56, blank=True)
    worlwide_gross_income = models.CharField(max_length=56, blank=True)
    metascore = models.FloatField(blank=True)
    reviews_from_users = models.FloatField(blank=True)
    reviews_from_critics = models.FloatField(blank=True)


    class Meta:
        verbose_name_plural = 'Movies'


    def __str__(self):
        return self.id if self.id else self.title



