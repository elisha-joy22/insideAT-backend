from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Video(models.Model):
    video_url = models.URLField()


class VideoMetadata(models.Model):
    video = models.ForeignKey(Video, related_name='metadata', on_delete=models.CASCADE)
    title = models.CharField(max_length=200),
    duration = models.DurationField,
    genre = models.ManyToManyField(Genre,related_name='metadata'),
    posted_date = models.DateTimeField(auto_now_add=True),
    language = models.CharField(max_length=200),
    upvotes = models.IntegerField,
    description = models.TextField,

    def __str__(self):
        return self.title



class VideoThumbnail(models.Model):
    video = models.OneToOneField(Video,related_name='thumbnails',on_delete=models.CASCADE)
    banner_image_url = models.URLField,
    potrait_image_url = models.URLField

    def __str__(self):
        return f'thumbnail for {self.video.title}'
    


class Participant(models.Model):
    video = models.ForeignKey(Video, related_name='participants', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    role = models.ForeignKey(Role, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.user.username} - {self.role}'
    


class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    reaction_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.comment[0:8]}...'
    

