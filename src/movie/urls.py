"""imdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import MovieDetailView, MovieListView, MovieRecentListView, MovieTopListView, MovieMostListView, \
    MovieCategory, MovieLanguage, MovieSearch

app_name = 'movie'
urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie-category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie-language'),
    path('search/', MovieSearch.as_view(), name='movie-search'),
    path('recent', MovieRecentListView.as_view(), name='movie-recent-list'),
    path('most', MovieMostListView.as_view(), name='movie-most-list'),
    path('top', MovieTopListView.as_view(), name='movie-top-list'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
]

