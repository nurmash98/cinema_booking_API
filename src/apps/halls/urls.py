from rest_framework.routers import DefaultRouter
from .views import HallViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'halls', HallViewSet, basename='halls')

urlpatterns = [
    path('', include(router.urls)),
]
