from django.contrib import admin

from inside_talks.models import Genre, Role, Language, VideoData, Resource, Participant, Comment
from inside_talks.forms import VideoDataForm,CommentForm,ParticipantForm 

# Inline Admin for VideoMetadata
class ResourceInline(admin.StackedInline):
    model = Resource
    extra = 1

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language',)




# Admin for VideoMetadata
@admin.register(VideoData)
class VideoDataAdmin(admin.ModelAdmin):
    form = VideoDataForm
    inlines = [ResourceInline]
    readonly_fields = ('likes',)



# Admin for Participant
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    form = ParticipantForm


# Admin for Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
    readonly_fields = ('posted_date',)
