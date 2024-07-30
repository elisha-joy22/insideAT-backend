from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inside_talks.views import GenreViewSet, VideoMetadataViewSet, VideoThumbnailViewSet


router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'video_metadata', VideoMetadataViewSet)
router.register(r'video_thumbnails', VideoThumbnailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
