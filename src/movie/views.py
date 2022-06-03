from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView, DetailView

from .models import Movie


class MovieListView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie
