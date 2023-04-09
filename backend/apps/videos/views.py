from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import VideoSerializer
from .models import Video


class VideoViewSet(ReadOnlyModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
