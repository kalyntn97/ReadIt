from django.shortcuts import render
from django.db.models.functions import Now
from .models import Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

class NoteList(LoginRequiredMixin, ListView):
  model = Note

  def get_queryset(self):
      return Note.objects.filter(user=self.request.user, expire_on__gt=Now()).order_by('-created_at')
  
class NoteDetail(LoginRequiredMixin, DetailView):
  model = Note

class NoteCreate(LoginRequiredMixin, CreateView):
  model = Note
  fields = ['title', 'content', 'expire_on']
  success_url = '/notes/'

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
  
class NoteUpdate(LoginRequiredMixin, UpdateView):
  model = Note
  fields = ['title', 'content', 'expire_on']

class NoteDelete(LoginRequiredMixin, DeleteView):
  model = Note
  success_url = '/notes/'

class Home(LoginView):
  template_name = 'home.html'

# Create your views here.
def about(request):
  return render(request, 'about.html')

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
