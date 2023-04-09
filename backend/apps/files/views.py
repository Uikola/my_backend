from rest_framework import viewsets
from .serializers import FileSerializer

from .models import File
from core.permissions import IsSubscriber


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [IsSubscriber,]