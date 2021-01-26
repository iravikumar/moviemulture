from django.urls import path

from .views import (
    MovieListAPIView, MovieDetailAPIView,
    MovieListListAPIView, MovieListDetailAPIView,
)

urlpatterns = [
    path('movies/', MovieListAPIView.as_view(),),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(),),
    path('movielist', MovieListListAPIView.as_view(),),
    path('movielist/<int:pk>/', MovieListDetailAPIView.as_view(),),
]
