from django.views.generic import ListView, DetailView

from .models import Movie, MovieLinks


class MovieListView(ListView):
    model = Movie

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(MovieListView, self).get_context_data()
        return ctx


class MovieRecentListView(MovieListView):
    queryset = Movie.objects.all().filter(status='R')


class MovieTopListView(MovieListView):
    queryset = Movie.objects.all().filter(status='T')


class MovieMostListView(MovieListView):
    queryset = Movie.objects.all().filter(status='M')


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
