from django import forms

from inside_talks.models import VideoData,Participant,Comment


class VideoDataForm(forms.ModelForm):
    class Meta:
        model = VideoData
        fields = '__all__'
        help_texts = {
            'duration': 'Enter the duration in Hour:Minute:Second format. For example, "1:30:45" for 1 hour, 30 minutes, and 45 seconds.',
        }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'