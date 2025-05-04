from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.PositiveIntegerField()
    seatsPerRow = models.PositiveIntegerField()

    def __str__(self):
        return self.name

