from rest_framework import serializers
from .models import Hall

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'

    