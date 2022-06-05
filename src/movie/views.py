from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView

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

    def dispatch(self, request, *args, **kwargs):
        self.category = self.kwargs['category']
        return super(MovieCategory, self).dispatch(request, *args, **kwargs)

    def __init__(self, **kwargs):
        super().__init__()
        self.category = None

    def get_queryset(self):
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(MovieCategory, self).get_context_data(**kwargs)
        ctx['movie_category'] = self.category
        return ctx


class MovieLanguage(ListView):
    model = Movie

    def dispatch(self, request, *args, **kwargs):
        self.language = self.kwargs['lang']
        return super(MovieLanguage, self).dispatch(request, *args, **kwargs)

    def __init__(self, **kwargs):
        super().__init__()
        self.language = None

    def get_queryset(self):
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(MovieLanguage, self).get_context_data(**kwargs)
        ctx['movie_language'] = self.language
        return ctx


class MovieSearch(ListView):
    model = Movie

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True

