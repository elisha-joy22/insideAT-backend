from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inside_talks.views import GenreViewSet, VideoDataViewSet


router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'video_data', VideoDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
