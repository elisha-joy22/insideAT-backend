from rest_framework import viewsets
from rest_framework.response import Response

from inside_talks.models import Genre, VideoData
from inside_talks.serializers import GenreSerializer, VideoDataSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class VideoDataViewSet(viewsets.ModelViewSet):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        suggestions = serializer.get_suggestions(instance)
        response_data = serializer.data
        response_data['suggestions'] = suggestions
        print("data",response_data)
        return Response(response_data)
        




