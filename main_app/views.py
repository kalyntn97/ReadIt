from django.shortcuts import render
from .models import Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

class NoteList(ListView):
  model = Note

class NoteDetail(DetailView):
  model = Note

class NoteCreate(CreateView):
  model = Note
  fields = ['title', 'content', 'expire_on']
  success_url = '/notes/'

class NoteUpdate(UpdateView):
  model = Note
  fields = ['title', 'content', 'expire_on']

class NoteDelete(DeleteView):
  model = Note
  success_url = '/notes/'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


