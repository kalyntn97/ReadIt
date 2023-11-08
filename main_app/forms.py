from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['title', 'content', 'expire_on']
    widgets = {
      'title': forms.Textarea(attrs={'placeholder': 'Title'}),
      'content': forms.Textarea(attrs={'placeholder': 'Enter content here'}),
      'expire_on': forms.DateInput(attrs={'placeholder': 'Enter expiration date (optional)'}),
    }