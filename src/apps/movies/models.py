from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Продолжительность в минутах")
    posterUrl = models.URLField(max_length=500, blank=True, null=True)
    release_date = models.DateField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    