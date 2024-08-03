from rest_framework import serializers
from inside_talks.models import Genre,VideoData,Comment,Participant,Resource


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['video_url','banner_image_url','portrait_image_url']


class VideoDataSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    language = serializers.SlugRelatedField(
        slug_field='language',
        read_only=True
    )
    resource = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    participants = serializers.SerializerMethodField()

    class Meta:
        model = VideoData
        fields = ['id','title', 'duration', 'genre', 'posted_date', 'language', 'likes', 'description','resource', 'comments','participants', ]

    def get_genre(self, obj):
        return [genre.name for genre in obj.genre.all()]
    
    def get_resource(self, obj):
        return ResourceSerializer(obj.resource).data
    
    def get_participants(self, obj):
        print("boo")
        print("\n")
        participants = Participant.objects.filter(video_data_id=obj.id).select_related('role')
        print("participants",participants)
        return ParticipantSerializer(participants, many=True).data

    def get_comments(self, obj):
        comments = Comment.objects.filter(video_data_id=obj.id)
        return CommentSerializer(comments, many=True).data

    def get_suggestions(self, obj):
        similar_videos = VideoData.objects.filter(genre__in=obj.genre.all()).exclude(id=obj.id).select_related('resource')[:6]
        print(obj)    
        return VideoDataSerializer(similar_videos, many=True).data



class ParticipantSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    role = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = Participant
        fields = ['user','role',]



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    class Meta:
        model = Comment
        fields = ['user', 'posted_date', 'comment']



