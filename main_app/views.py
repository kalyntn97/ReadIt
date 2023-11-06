from django.shortcuts import render
from .models import Note
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

class NoteList(ListView):
  model = Note

class NoteCreate(CreateView):
  model = Note
  fields = ['title', 'content', 'expire_on']


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


