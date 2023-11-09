from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['title', 'content', 'expire_on']
    widgets = {
      'title': forms.Textarea(attrs={'placeholder': 'Title'}),
      'content': forms.Textarea(attrs={'placeholder': 'Enter content here'}),
      'expire_on': forms.DateInput(attrs={'placeholder': 'Enter expiration date (optional)'}),
    }

class LoginForm(forms.Form):
  login_username = forms.CharField(label='Username', max_length=63)
  login_password = forms.CharField(label='Password', max_length=63, widget=forms.PasswordInput)