from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Hall
from .serializers import HallSerializer
from .permissions import IsAdminOrReadOnly

class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsAdminOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        Response({"message": "Зал успешно создан", "id": serializer.data.get("id")}, status=status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Информация о зале обновлена"})
    
    def destroy(self, request, *args, **kwargs):
        instance =  self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Зал успешно удалён"})
    
