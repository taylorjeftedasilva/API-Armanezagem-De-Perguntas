from django.contrib.auth.models import UserManager
from django.urls import path, include
from .models import Game
from .views import GameViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register('game', GameViewSet)


urlpatterns = [
    path('', include(router.urls)),
]