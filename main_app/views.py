# import requests
from django import forms
from django.shortcuts import render, redirect
from django.db.models.functions import Now
from .models import Note
# from .forms import NoteForm
# from .forms import LoginForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.conf import settings
# import os

class NoteList(LoginRequiredMixin, ListView):
  model = Note

  def get_queryset(self):
    #save - delete expired notes, doesn't work with gTTS yet
    Note.objects.filter(expire_on__lt=Now()).delete()
    #get notes that are not expired or do not have exp. date
    queryset_not_expired = Note.objects.filter(expire_on__gt=Now()) | Note.objects.filter(expire_on__isnull=True)
    #only show user's notes
    return queryset_not_expired.filter(user=self.request.user).order_by('-created_at')
  
class NoteCreate(LoginRequiredMixin, CreateView):
  model = Note
  fields = ['title', 'content', 'expire_on']
  success_url = '/notes/'

  def get_form(self, form_class=None):
    if form_class is None:
        form_class = self.get_form_class()

    form = super(NoteCreate, self).get_form(form_class)
    form.fields['title'].widget = forms.Textarea(attrs={'placeholder': 'Enter title'})
    form.fields['content'].widget = forms.Textarea(attrs={'placeholder': 'Enter content'})
    form.fields['expire_on'].widget = forms.DateInput(attrs={'placeholder': 'Enter expiration date (optional)'})
    return form

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class NoteDetail(DetailView):
  model = Note

class NoteUpdate(LoginRequiredMixin, UpdateView):
  model = Note
  fields = ['title', 'content', 'expire_on']

class NoteDelete(LoginRequiredMixin, DeleteView):
  model = Note
  success_url = '/notes/'

class Home(LoginView):
  template_name = 'home.html'

  def get_form(self, form_class=None):
    if form_class is None:
        form_class = self.get_form_class()

    form = super(Home, self).get_form(form_class)
    form.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Your username'})
    form.fields['password'].widget = forms.TextInput(attrs={'placeholder': 'Your password'})
    return form

# Create your views here.
def about(request):
  return render(request, 'about.html')

#save - login and signup in same view
# def home(request):
#   error_message_signin = ''
#   error_message_signup = ''
#   if request.method == 'POST':
#     if 'signin' in request.POST:
#       form_signin = LoginForm(request.POST, auto_id="login_%s")
#       if form_signin.is_valid:
#         username = request.POST.get('login_username')
#         password = request.POST.get('login_password')
#         user = authenticate(username=username, password=password)
#         if user:
#           login(request, user)
#           return redirect('/')
#         else:
#           error_message_signin = 'Invalid username or password.'
#       else: 
#           error_message_signin = 'Invalid username or password.'

#     elif 'signup' in request.POST:
#       form_signup = UserCreationForm(request.POST, auto_id="register_%s")
#       if form_signup.is_valid:
#         user = form_signup.save()
#         login(request, user)
#         return redirect('/')
#       else:
#         error_message_signup = 'Invalid Signup - Try again'

#   form_signin = LoginForm()
#   form_signup = UserCreationForm()

#   context = {'form_signin': form_signin, 'form_signup': form_signup, 'error_message_signin': error_message_signin, 'error_message_signup': error_message_signup}
#   return render(request, 'home.html', context)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('note-index')
    else:
      error_message = 'Invalid Signup - Try again'
  form = UserCreationForm()
  context = { 'form': form, 'error-message': error_message }

  return render(request, 'signup.html', context)

#save for future storage options
# def note_detail(request, note_id):
#   note = Note.objects.get(id=note_id)
#   #covert content to speech with gTTS
#   tts = gTTS(text=(note.title + note.content), lang='en')
#   audio_file_name = f'{note.title}.mp3'
#   audio_folder_path = os.path.join(settings.MEDIA_ROOT, 'audio')
#   os.makedirs(audio_folder_path, exist_ok=True)
#   audio_file_path = os.path.join(audio_folder_path, audio_file_name)
#   tts.save(audio_file_path)
#   #save audio file to default storage
#   with open(audio_file_path, 'rb') as f:
#     default_storage.save(f'audio/{audio_file_name}', ContentFile(f.read()))
#   #pass content to template
#   context = {
#     'note': note,
#     'audio_file_url': default_storage.url(f'audio/{audio_file_name}')
#   }
  # return render(request, 'note_detail.html', {'note': note})

