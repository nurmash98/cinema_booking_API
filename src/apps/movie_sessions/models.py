from django.db import models
class Session(models.Model):
    movieId = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    hallId = models.ForeignKey('halls.Hall', on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    price = models.PositiveIntegerField()
    