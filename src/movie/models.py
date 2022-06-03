from django.db import models


# Create your models here.


class Movie(models.Model):
    CATEGORY_CHOICES = (
        ('Action', 'ACTION'),
        ('Drama', 'DRAMA'),
        ('Comedy', 'COMEDY'),
        ('Romance', 'ROMANCE'),
        ('Horror', 'HORROR'),
    )
    LANGUAGE_CHOICES = (
        ('EN', 'ENGLISH'),
        ('AR', 'ARABIC')
    )
    STATUS_CHOICES = (
        ('R', 'RECENTLY ADDED'),
        ('M', 'MOST WATCHED'),
        ('T', 'TOP RATED')
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES, default='Action')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='R')
    cast = models.CharField(max_length=255)
    year_of_production = models.DateField()
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class MovieLinks(models.Model):
    Link_CHOISES = (
        ('D', 'DOWNLOAD LINK'),
        ('W', 'WATCH LINK'),
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='movie_watch_link')
    link = models.URLField()
    type = models.CharField(choices=Link_CHOISES, max_length=1, default='D')

    def __str__(self):
        return self.movie.title