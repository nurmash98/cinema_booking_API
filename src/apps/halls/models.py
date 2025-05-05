from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField()
    seatsPerRow = models.PositiveIntegerField()

    def __str__(self):
        return self.name

