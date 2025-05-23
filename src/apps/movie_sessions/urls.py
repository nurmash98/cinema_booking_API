
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SessionViewSet

router = DefaultRouter()
router.register('sessions', SessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]
