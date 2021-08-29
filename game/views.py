from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from .serializer import GameSerializer
from .models import Game

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class GameViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated|ReadOnly] 
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def list(self, request):
        queryset = Game.objects.all()
        data =GameSerializer(queryset, many=True).data
        return Response(data, status.HTTP_200_OK)