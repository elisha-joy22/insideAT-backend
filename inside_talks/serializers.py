from rest_framework import serializers
from inside_talks.models import Genre,VideoData,Comment,Participant


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class VideoMetadataSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = VideoData
        fields = ['title', 'duration', 'genres', 'posted_date', 'language', 'likes', 'description']


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['video','user','role']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['video', 'user', 'posted_date', 'comment']



