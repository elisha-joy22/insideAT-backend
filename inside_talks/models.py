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


class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language


class VideoData(models.Model):
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    genre = models.ManyToManyField(Genre, related_name='films')
    posted_date = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(
                            Language,
                            related_name='films',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True
    )
    likes = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title




class Resource(models.Model):
    video_data = models.OneToOneField(VideoData, related_name="resource", on_delete=models.CASCADE)
    video_url = models.URLField()
    banner_image_url = models.URLField()
    portrait_image_url = models.URLField()


    def __str__(self):
        return f"{self.video_data.title} - Resources"


class Participant(models.Model):
    video_data = models.ForeignKey(VideoData, related_name='participants', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.user.username} - {self.role}'



class Comment(models.Model):
    video_data = models.ForeignKey(VideoData, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.user.username} - {self.comment[:8]}...'
    

