from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.views.generic import ListView, DetailView

from .models import Movie, MovieLinks


class MovieListView(ListView):
    model = Movie

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(MovieListView, self).get_context_data()
        ctx['top'] = Movie.objects.all().filter(status='T')
        ctx['most'] = Movie.objects.all().filter(status='M')
        ctx['recent'] = Movie.objects.all().filter(status='R')
        return ctx


class MovieRecentListView(ListView):
    queryset = Movie.objects.all().filter(status='R')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(MovieRecentListView, self).get_context_data()
        ctx['recent'] = Movie.objects.all().filter(status='R')
        return ctx


class MovieTopListView(ListView):
    queryset = Movie.objects.all().filter(status='T')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(MovieTopListView, self).get_context_data()
        ctx['top'] = Movie.objects.all().filter(status='T')
        return ctx


class MovieMostListView(ListView):
    queryset = Movie.objects.all().filter(status='M')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(MovieMostListView, self).get_context_data()
        ctx['most'] = Movie.objects.all().filter(status='M')
        return ctx


class MovieDetailView(DetailView):
    model = Movie

    def get_object(self, queryset=None):
        obj = super(MovieDetailView, self).get_object()
        return obj

    def get_context_data(self, **kwargs):
        ctx = super(MovieDetailView, self).get_context_data()
        ctx['links'] = MovieLinks.objects.filter(movie=self.get_object())
        movie = self.get_object()
        movie.view_count += 1
        movie.save()
        return ctx


class MovieCategory(ListView):
    model = Movie

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(MovieCategory, self).get_context_data(**kwargs)
        ctx['movie_category'] = self.category
        return ctx
