from django.contrib import admin
from .models import Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movieId', 'hallId', 'startTime', 'price')
    search_fields = ('startTime',)
    list_filter = ('price',)
