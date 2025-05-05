# apps/sessions/views.py
from rest_framework import viewsets
from .models import Session
from .serializers import SessionSerializer
from .permissions import IsAdminOrReadOnly

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAdminOrReadOnly]
