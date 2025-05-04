from rest_framework import generics, status
from .models import User
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "message": "Пользователь успешно зарегистрирован",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "role": user.role,
                }
            }, status=status.HTTP_201_CREATED
        )

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        tokens = serializer.validated_data

        return Response({
            "message": "Вход выполнен успешно",
            "access": tokens.get("access"),
            "refresh": tokens.get("refresh"),
            "user": {
                "id": user.id,
                "email": user.email,
                "role": user.role,
            }
        }, status=status.HTTP_200_OK)


__all__ = ['RegisterView', 'MyTokenObtainPairView']
