from .models import Movie


def slider_movies(request):
    movies = Movie.objects.all().order_by('created')[0:10]
    return {'slider_movies': movies}
