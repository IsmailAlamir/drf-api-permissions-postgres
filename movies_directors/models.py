from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Movie(models.Model):
    movie = models.CharField(max_length=255)
    description = models.TextField()
    release = models.IntegerField()
    director = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.movie

class Director(models.Model):
    director = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField()
    Awards = models.IntegerField()
    
    def __str__(self):
        return self.description
