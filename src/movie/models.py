from django.db import models


# Create your models here.


class Movie(models.Model):
    CATEGORY_CHOICES = (
        ('A', 'ACTION'),
        ('D', 'DRAMA'),
        ('C', 'COMEDY'),
        ('R', 'ROMANCE'),
        ('H', 'HORROR'),
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
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='A')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='R')
    year_of_production = models.DateField()
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
