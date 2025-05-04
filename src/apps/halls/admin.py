from django.contrib import admin
from .models import Hall

@admin.register(Hall)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'rows', 'seatsPerRow')
    search_fields = ('name',)
    list_filter = ('rows',)
