from django import forms
from .models import Event, RSVP, Post   

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_time', 'end_time']

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['status']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']  # Include the image field