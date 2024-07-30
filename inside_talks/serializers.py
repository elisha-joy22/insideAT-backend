from rest_framework import serializers
from inside_talks.models import Genre,VideoMetadata,VideoThumbnail,Comment,Participant


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class VideoMetadataSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = VideoMetadata
        fields = ['title', 'duration', 'genres', 'posted_date', 'language', 'likes', 'description']


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['video','user','role']



class VideoThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoThumbnail
        fields = ['video', 'banner_image_url', 'portrait_image_url']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['video', 'user', 'posted_date', 'comment']



