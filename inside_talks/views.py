from rest_framework import viewsets
from inside_talks.models import Genre, VideoMetadata, VideoThumbnail
from inside_talks.serializers import GenreSerializer, VideoMetadataSerializer, VideoThumbnailSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class VideoMetadataViewSet(viewsets.ModelViewSet):
    queryset = VideoMetadata.objects.all()
    serializer_class = VideoMetadataSerializer


class VideoThumbnailViewSet(viewsets.ModelViewSet):
    queryset = VideoThumbnail.objects.all()
    serializer_class = VideoThumbnailSerializer




